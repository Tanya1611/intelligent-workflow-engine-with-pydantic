"""Testing Tools for their Behaviour """

import pytest

from app.tools.answer_tool import AnswerTool
from app.tools.search_tool import SearchTool
from app.tools.summarize_tool import SummarizeTool


def test_summarize_short_text():
    tool = SummarizeTool()

    result = tool.execute("Full form of RAG is Retrieval Augmented Generation")

    assert result == "Full form of RAG is Retrieval Augmented Generation"


def test_summarize_empty_text():
    tool = SummarizeTool()

    with pytest.raises(ValueError):
        tool.execute(" ")


def test_search_tool():
    tool = SearchTool()

    result = tool.execute("Python")

    assert "Python" in result


def test_search_empty_query():
    tool = SearchTool()

    with pytest.raises(ValueError):
        tool.execute("   ")


def test_answer_tool():
    tool = AnswerTool()

    result = tool.execute("What is Python?")

    assert result
