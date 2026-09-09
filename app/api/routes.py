from fastapi import APIRouter, Depends

from app.engine.workflow_engine import WorkflowEngine
from app.models.request import UserRequest
from app.models.response import WorkflowResponse


router = APIRouter(prefix="/workflow", tags=["Workflow"])


def get_workflow_engine() -> WorkflowEngine:

    """Provides the workflow engine to API endpoints."""
    return WorkflowEngine()


@router.post("/run", response_model=WorkflowResponse)
def run_workflow(request: UserRequest, engine: WorkflowEngine = Depends(get_workflow_engine)) -> WorkflowResponse:
    """
    Accepts a workflow request and returns the execution result.

    FastAPI uses the Pydantic UserRequest model to validate the incoming request before passing it to the workflow engine.
    """

    return engine.run(request)