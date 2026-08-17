import logging
import time

from app.models.execution import ExecutionResult
from app.models.task import WorkflowTask
from app.registry.tool_registry import ToolRegistry

logger = logging.getLogger(__name__)

class ExecutorNode:
    '''
    Executes workflow tasks by retrieving the appropriate tool from the Tool Registry.

    The Executor coordinates task execution but does not depend on the internal implementation of individual tools.
    '''

    def __init__(self, tool_registry: ToolRegistry):
        self.tool_registry = tool_registry

    def process(self, task: WorkflowTask) -> ExecutionResult:

        start = time.time()
        logger.info("Executing task %s: %s", task.task_id, task.task_name)

        try:
            tool = self.tool_registry.get_tool(task.task_type)
            logger.info("Selected tool: %s", tool.__class__.__name__)

            output = tool.execute(task.input_data)
            execution_time = round(time.time() - start, 5)

            logger.info("Task %s completd successfully.", task.task_id)

            return ExecutionResult(
                task_id=task.task_id,
                success=True,
                output=output,
                execution_time=execution_time
            )

        except Exception as error:
            execution_time = round(time.time() - start, 5)

            logger.exception("Task %s failed.", task.task_id)

            # Return a structured failure result instead of exposing an unstructured exception to the next workflow stage.
            return ExecutionResult(
                task_id=task.task_id,
                success=False,
                output=str(error),
                execution_time=execution_time
            )