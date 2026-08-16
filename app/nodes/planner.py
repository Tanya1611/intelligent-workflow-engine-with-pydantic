import logging

from app.core.config import settings
from app.models.intent import IntentResult, IntentType
from app.models.task import TaskType, WorkflowTask


logger = logging.getLogger(__name__)


class PlannerNode:
    '''
    Converts the detected intent into structured workflow tasks.

    The Planner decides what work should be performed but does not execute the tasks itself.
    '''

    def process(self, intent: IntentResult, message: str) -> list[WorkflowTask]:

        # Collect all tasks created for the current workflow.
        tasks: list[WorkflowTask] = []

        if intent.intent == IntentType.QUESTION:
            tasks.append(
                WorkflowTask(
                    task_id=1,
                    task_name="Answer Question",
                    task_type=TaskType.ANSWER,
                    priority=5,
                    input_data=message,
                )
            )
        elif intent.intent == IntentType.TASK:
            tasks.append(
                WorkflowTask(
                    task_id=1,
                    task_name="Summarize Text",
                    task_type=TaskType.SUMMARIZE,
                    priority=5,
                    input_data=message,
                )
            )
        elif intent.intent == IntentType.SEARCH:
            tasks.append(
                WorkflowTask(
                    task_id=1,
                    task_name="Search Information",
                    task_type=TaskType.SEARCH,
                    priority=4,
                    input_data=message,
                )
            )

        # Enforce the configured limit before returning workflow tasks.
        if len(tasks) > settings.max_tasks:
            raise ValueError(
                f"Workflow contains {len(tasks)} tasks. "
                f"Maximum allowed is {settings.max_tasks}."
            )

        logger.info("Planner created %d task(s).", len(tasks))

        return tasks