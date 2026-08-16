'''
The parser's only job is to understand the intention.
'''

import logging

from app.models.request import UserRequest
from app.models.intent import IntentResult, IntentType

logger = logging.getLogger(__name__)

class ParserNode:
    '''
    Reads the user's message and identifies the intent of the request.

    The output is a structured IntentResult that can be used by the next stage of the workflow.
    '''

    def process(self, request: UserRequest) -> IntentResult:

        # Normalize the message to make keyword checks case-insensitive.
        message = request.message.lower().strip()

        if not message:
            return IntentResult(
                intent=IntentType.UNKNOWN,
                confidence=1.0,
                reason="Empty message."
            )

        if "summarize" in message or "summary" in message:
            intent = IntentResult(
                intent = IntentType.TASK,
                confidence = 0.95,
                reason = "User requested Summarization."
            )
        elif "search" in message or "find" in message:
            intent = IntentResult(
                intent = IntentType.SEARCH,
                confidence = 0.8,
                reason = "User requested a search."
            )
        elif "what" in message or message.endswith("?") or "how" in message:
            intent = IntentResult(
                intent = IntentType.QUESTION,
                confidence = 0.92,
                reason = "User asked a Question."
            )
        else:
            intent = IntentResult(
                intent = IntentType.UNKNOWN,
                confidence = 0.5,
                reason = "Could not determine the user's intent"
            )

        logger.info("Detected intent: %s", intent.intent.value)

        return intent