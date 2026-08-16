from pydantic import BaseModel, Field

from app.models.execution import ExecutionResult

class WorkflowResponse(BaseModel):
    '''
    Represents the final structured output returned by the workflow.

    It combines the overall workflow status with the results produced by individual task executions.
    '''

    success: bool
    message: str = Field(min_length=1)

    # Collects the results produced by all executed workflow tasks.
    results: list[ExecutionResult]