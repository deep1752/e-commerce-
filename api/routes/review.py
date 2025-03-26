from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from api.database.connection import get_db
from api.database.schemas.review import ReviewResponse,ReviewCreate
from api.crud.review import create_review, get_all_reviews

# Creating an API router instance for handling user-related routes
router = APIRouter()

@router.post("/add", response_model=ReviewResponse)
def add(review: ReviewCreate , db:Session = Depends(get_db)):
    
    return create_review(db,review)

@router.get("/all", response_model=List[ReviewResponse])
def list_review(db: Session = Depends(get_db)):
    return get_all_reviews(db)
