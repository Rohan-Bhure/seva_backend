from pydantic import BaseModel, Field
from typing import Optional

class UserCreate(BaseModel):
    username: str = Field(..., min_length=2)
    mobile: str = Field(..., min_length=10, max_length=10)

class UserUpdate(BaseModel):
    username: Optional[str]
    mobile: Optional[str]

class UserResponse(BaseModel):
    id: str
    username: str
    mobile: str