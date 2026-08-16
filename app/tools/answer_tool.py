class AnswerTool:
    """
    Handles question requests.

    The current workflow engine does not contain an LLM.
    AI-based answering will be implemented in the separate AI-agent project.
    """

    def execute(self, question: str) -> str:

        question = question.strip()

        if not question:
            raise ValueError("Question cannot be empty.")

        # Return the current workflow response for question requests.
        return (
            "This workflow engine currently handles structured workflow execution. "
            "AI-powered question answering will be added in the AI-agent project."
        )