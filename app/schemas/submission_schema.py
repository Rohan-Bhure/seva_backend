from pydantic import BaseModel, Field
from datetime import date, datetime

class SubmissionCreate(BaseModel):
    category: str
    subcategory: str
    userId: str
    username: str
    date: date

class SubmissionResponse(BaseModel):
    id: str
    category: str
    subcategory: str
    userId: str
    username: str
    date: date
    createdAt: datetime