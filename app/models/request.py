from pydantic import BaseModel, Field, ConfigDict, field_validator
from datetime import datetime

class UserRequest(BaseModel):
    '''
    Represents the validated input boundary of the workflow.

    Every incoming request is converted into a structured object before it moves to the parsing and planning stages.
    '''

    # Reject unexpected fields to keep the input contract strict.
    model_config = ConfigDict(extra="forbid")

    request_id: str = Field(min_length=1)
    username: str = Field(min_length = 1, max_length=100)
    message: str = Field(min_length = 1, max_length = 5000)
    timestamp: datetime

    @field_validator("message")
    @classmethod
    def message_must_not_blank(cls, value: str) -> str:

        value = value.strip()
        if not value:
            raise ValueError("Message cannot be blank.")

        return value


