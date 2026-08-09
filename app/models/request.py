# Getting user request in a defined way

from pydantic import BaseModel, Field, ConfigDict, field_validator
from datetime import datetime

class UserRequest(BaseModel):

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


