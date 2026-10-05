"""Testing Tool Registry"""

from app.models.task import TaskType, WorkflowTask
from app.nodes.executor import ExecutorNode
from app.registry.tool_registry import ToolRegistry


def test_executor_success():

    executor = ExecutorNode(
        ToolRegistry()
    )

    task = WorkflowTask(
        task_id=1,
        task_name="Search",
        task_type=TaskType.SEARCH,
        priority=4,
        input_data="Python",
    )

    result = executor.process(task)

    assert result.success is True
    assert result.task_id == 1
    assert result.output
    assert result.execution_time >= 0
