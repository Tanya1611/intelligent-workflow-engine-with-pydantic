from enum import Enum

from pydantic import BaseModel, Field

class IntentType(str, Enum):
    QUESTION = "question"
    TASK = "task"
    SEARCH = "search"
    UNKNOWN = "unknown"

class IntentResult(BaseModel):
    '''
    Represents the structured output produced by the Parser.

    It separates understanding the user's request from deciding how the workflow should execute it.
    '''
    
    intent: IntentType
    confidence: float = Field(ge=0.0, le=1.0)
    reason: str = Field(min_length=1)