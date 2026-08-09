# Final Response model for the execution of a workflow step

from pydantic import BaseModel, Field

from app.models.execution import ExecutionResult

class WorkflowResponse(BaseModel):
    success: bool
    message: str = Field(min_length=1)
    results: list[ExecutionResult]