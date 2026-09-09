from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.api.routes import router
from app.core.exceptions import InvalidWorkflowError


app = FastAPI(
    title="Modular Intelligent Workflow Engine",
    description="API layer for the modular workflow engine.",
    version="1.0.0",
)


app.include_router(router)


@app.get("/workflow_checker")
def health_check() -> dict[str, str]:
    """Basic endpoint to confirm that the service is running."""
    return {
        "status": "Running"
    }


@app.exception_handler(InvalidWorkflowError)
async def workflow_error_handler(request: Request, exc: InvalidWorkflowError) -> JSONResponse:

    """Converts workflow failures into a consistent API response."""

    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": str(exc),
            "results": [],
        },
    )