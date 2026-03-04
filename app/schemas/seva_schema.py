from pydantic import BaseModel, Field
from typing import Optional

class SevaCreate(BaseModel):
    category: str = Field(..., min_length=2)
    subcategory: str = Field(..., min_length=2)

class SevaUpdate(BaseModel):
    category: Optional[str]
    subcategory: Optional[str]

class SevaResponse(BaseModel):
    id: str
    category: str
    subcategory: str