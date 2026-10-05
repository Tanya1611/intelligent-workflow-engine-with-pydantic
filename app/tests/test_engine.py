"""Testing whole workflow"""

from datetime import datetime

from app.engine.workflow_engine import WorkflowEngine
from app.models.request import UserRequest


def test_workflow_engine_question():

    engine = WorkflowEngine()

    request = UserRequest(
        request_id="REQ-TEST",
        username="tester",
        message="What is Python?",
        timestamp=datetime.now(),
    )

    response = engine.run(request)

    assert response.success is True
    assert len(response.results) == 1
    assert response.results[0].success is True


def test_workflow_engine_search():

    engine = WorkflowEngine()

    request = UserRequest(
        request_id="REQ-TEST",
        username="tester",
        message="Search for Python",
        timestamp=datetime.now(),
    )

    response = engine.run(request)

    assert response.success is True
    assert len(response.results) == 1
    assert "Python" in response.results[0].output
