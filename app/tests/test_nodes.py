"""Testing Parser and Planner nodes"""

from datetime import datetime

from app.models.request import UserRequest
from app.models.intent import IntentType
from app.models.task import TaskType
from app.nodes.parser import ParserNode
from app.nodes.planner import PlannerNode


def create_request(message: str) -> UserRequest:
    return UserRequest(
        request_id="REQ-TEST",
        username="tester",
        message=message,
        timestamp=datetime.now(),
    )


def test_parser_detects_question():
    parser = ParserNode()

    request = create_request("What is Python?")

    result = parser.process(request)

    assert result.intent == IntentType.QUESTION
    assert result.confidence > 0


def test_parser_detects_search():
    parser = ParserNode()

    request = create_request("Search for Python")

    result = parser.process(request)

    assert result.intent == IntentType.SEARCH


def test_parser_detects_summarization():
    parser = ParserNode()

    request = create_request("Summarize this text")

    result = parser.process(request)

    assert result.intent == IntentType.TASK


def test_parser_detects_unknown():
    parser = ParserNode()

    request = create_request("Hello there")

    result = parser.process(request)

    assert result.intent == IntentType.UNKNOWN


def test_planner_creates_answer_task():
    planner = PlannerNode()

    intent = ParserNode().process(
        create_request("What is Python?")
    )

    tasks = planner.process(
        intent,
        "What is Python?"
    )

    assert len(tasks) == 1
    assert tasks[0].task_type == TaskType.ANSWER
    assert tasks[0].priority == 5
