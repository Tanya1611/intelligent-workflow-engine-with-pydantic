class SummarizeTool:
    '''
    Creates a simple deterministic summary.

    The current implementation does not use an LLM. It follows a predictable rule-based approach for summarization.
    '''

    def execute(self, text: str) -> str:

        text = text.strip()

        if not text:
            raise ValueError(
                "Cannot summarize empty text."
            )

        words = text.split()
        
        if len(words) <= 20:
            return text  # If the text is short, return it as is.
        else:
            return " ".join(words[:20])+"..."  # Return the first 20 words as a summary.