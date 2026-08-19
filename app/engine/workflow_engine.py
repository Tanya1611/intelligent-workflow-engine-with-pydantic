import logging

from app.core.exceptions import InvalidWorkflowError
from app.models.request import UserRequest
from app.models.response import WorkflowResponse

from app.nodes.parser import ParserNode
from app.nodes.planner import PlannerNode
from app.nodes.executor import ExecutorNode
from app.nodes.validator import ValidatorNode

from app.registry.tool_registry import ToolRegistry

logger = logging.getLogger(__name__)

class WorkflowEngine:
    """
    Orchestrates the complete workflow from request processing to the final structured response.

    The engine coordinates the workflow stages but delegates the actual work to specialized components.
    """

    def __init__(self):
        # Initialize the components required for each workflow stage.
        self.parser = ParserNode()
        self.planner = PlannerNode()

        # Create the tool registry and provide it to the Executor.
        self.tool_registry = ToolRegistry() 
        self.executor = ExecutorNode(self.tool_registry)
        self.validator = ValidatorNode()

    def run(self, request: UserRequest) -> WorkflowResponse:

        logger.info("Starting workflow: %s", request.request_id)

        try:
            # Step 1 : Understand the request
            intent = self.parser.process(request)

            # Step 2 : Plans the tasks based on the identified intent
            tasks = self.planner.process(intent, request.message)

            # Stop the workflow when no executable task can be created.
            if not tasks:
                logger.warning("No executable tasks created.")
                return WorkflowResponse(
                    success=False,
                    message="Unable to process the request. Please provide a valid request.",
                    results=[]
                )

            # Collect the result of each successfully processed task.
            results =[]

            # Step 3 : Execute each task and validate the results
            for task in tasks:
                result = self.executor.process(task)

                # Step 4: Validate the execution result
                is_valid = self.validator.process(result)

                if not is_valid:
                    logger.error("Validation failed for task %s.", task.task_id)
                    return WorkflowResponse(
                        success=False,
                        message=f"Execution failed for task {task.task_name}.",
                        results=results+[result]
                    )
                results.append(result)

            logger.info("Workflow %s completed succesfully.", request.request_id)

            # Step 5: Return the final response containing all task results.
            return  WorkflowResponse(
                success=True,
                message="Workflow executed successfully.",
                results=results
            )
        
        except Exception as error:
            logger.exception("Workflow %s failed!", request.request_id)

            raise InvalidWorkflowError(f"Workflow failed : {error}") from error
    