from pydantic import BaseModel, Field

class ExecutionResult(BaseModel):
    task_id: int = Field(ge=1)
    success: bool
    output: str
    execution_time: float = Field(ge=0)
