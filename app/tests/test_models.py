"""Testing Pydantic Contracts"""

from datetime import datetime
import pytest
from pydantic import ValidationError

from app.models.request import UserRequest
from app.models.task import TaskType, WorkflowTask


def test_valid_request():
    request = UserRequest(
        request_id="REQ-001",
        username="test_user",
        message="What is Python?",
        timestamp=datetime.now(),
    )

    assert request.request_id == "REQ-001"
    assert request.message == "What is Python?"


def test_blank_message_rejected():
    with pytest.raises(ValidationError):
        UserRequest(
            request_id="REQ-001",
            username="test_user",
            message="   ",
            timestamp=datetime.now(),
        )


def test_extra_field_rejected():
    with pytest.raises(ValidationError):
        UserRequest(
            request_id="REQ-001",
            username="test_user",
            message="What is Python?",
            timestamp=datetime.now(),
            unexpected_field="not allowed",
        )


def test_invalid_priority_rejected():
    with pytest.raises(ValidationError):
        WorkflowTask(
            task_id=1,
            task_name="Search",
            task_type=TaskType.SEARCH,
            priority=10,
            input_data="Python",
        )
