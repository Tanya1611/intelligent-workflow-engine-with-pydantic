from app.core.exceptions import ToolNotFoundError
from app.models.task import TaskType

from app.tools.answer_tool import AnswerTool
from app.tools.summarize_tool import SummarizeTool
from app.tools.search_tool import SearchTool


class ToolRegistry:
    """
    Maps task types to the tools that can execute them.

    It keeps tool selection separate from the Executor so that the execution flow does not need to know individual tool implementations.
    """

    def __init__(self):

        # Register each supported task type with its corresponding tool.
        self.tools = {
            TaskType.ANSWER: AnswerTool(),
            TaskType.SUMMARIZE: SummarizeTool(),
            TaskType.SEARCH: SearchTool(),
        }

    def get_tool(self, task_type: TaskType):

        # Look up the tool responsible for the requested task type.
        tool = self.tools.get(task_type)

        if tool is None:
            raise ToolNotFoundError(
                f"No tool registered for task type: {task_type}"
            )

        return tool