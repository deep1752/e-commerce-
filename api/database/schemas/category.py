from pydantic import BaseModel
from datetime import datetime

# User creation schema
class CategoryCreate(BaseModel):

    name: str
    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()
# Response model (excluding sensitive data)
class CategoryResponse(BaseModel):

    id: int
    name: str
    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()

class CategoryUpdate(BaseModel):

    name : str

    class Config:
        from_attributes = True

