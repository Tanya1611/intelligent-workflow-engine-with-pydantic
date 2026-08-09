# Return intent type
# enum se label lgadia - yehi koi vlaue choose honi chiye

from enum import Enum

from pydantic import BaseModel, Field

class IntentType(str, Enum):
    QUESTION = "question"
    TASK = "task"
    SEARCH = "search"
    UNKNOWN = "unknown"

class IntentResult(BaseModel):
    intent_type: IntentType
    confidence: float = Field(ge=0.0, le=1.0)
    reason: str = Field(min_length=1)