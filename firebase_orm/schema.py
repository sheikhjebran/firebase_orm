from pydantic import BaseModel, Field
from typing import Optional


class UserSchema(BaseModel):
    id: str
    name: str = Field(..., min_length=3)
    age: Optional[int] = Field(None, ge=0, le=120)
    email: Optional[str] = None
