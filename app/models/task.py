from enum import Enum
from pydantic import BaseModel, ConfigDict, Field

class TaskType(str, Enum):
    ANSWER = "answer"
    SEARCH = "search"
    SUMMARIZE = "summarize"

class WorkflowTask(BaseModel):
    '''
    Represents a structured unit of work created by the Planner.

    A task describes what the system should execute after the user's intent has been understood.
    '''

    model_config = ConfigDict(extra="forbid")

    task_id: int = Field(ge=1)
    task_name: str = Field(
        min_length=1,
        max_length=100
    )
    task_type: TaskType
    priority: int = Field(ge=1, le=5)
    input_data: str = Field(min_length=1)