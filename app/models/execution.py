from pydantic import BaseModel, Field

class ExecutionResult(BaseModel):
    '''
    Represents the structured result returned after a workflow task has been executed.

    It provides a consistent contract for both successful and unsuccessful task executions.
    '''

    task_id: int = Field(ge=1)
    success: bool
    output: str
    execution_time: float = Field(ge=0)
