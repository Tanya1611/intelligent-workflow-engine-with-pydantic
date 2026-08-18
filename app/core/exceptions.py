class WorkflowError(Exception):
    """
    Base exception for errors related to the workflow engine.

    It provides a common application-level error hierarchy for
    workflow-specific failures.
    """

class ToolNotFoundError(WorkflowError):
    """Raise when a requested tool is not registered."""

class ToolExecutionError(WorkflowError):
    """Raised when a tool fails during execution."""

class InvalidWorkflowError(WorkflowError):
    """Raised when a workflow cannot be created."""