from datetime import datetime

from app.core.logging_config import configure_logging
from app.engine.workflow_engine import WorkflowEngine
from app.models.request import UserRequest

def main():
    """
    Starts the application and demonstrates the complete workflow.

    It configures logging, creates a validated user request,
    runs the workflow, and prints the final structured response.
    """

    # Configure application-wide logging before the workflow starts.
    configure_logging()

    request = UserRequest(
        request_id = "REQ-001",
        username = "test_user",
        message = "Summarize : wheels on thr bus go round and round round and orund round and round",
        timestamp = datetime.now()
    )

    # Create the central orchestrator responsible for running the workflow.
    engine = WorkflowEngine()

    # Run the request through the complete workflow.
    response = engine.run(request)

    # Display the final workflow response in readable JSON format.
    print("\nFINAL RESPONSE")
    print("=" * 50)
    print(response.model_dump_json(indent=2))


if __name__ == "__main__":
    main()