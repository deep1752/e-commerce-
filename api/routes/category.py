from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from api.database.connection import get_db
from api.database.schemas.category import CategoryResponse, CategoryCreate, CategoryUpdate
from api.crud.category import create_category,delete_category, update_category, get_all_categories

# Creating an API router instance for handling user-related routes
router = APIRouter()

@router.post("/add", response_model=CategoryResponse)
def add(category: CategoryCreate , db:Session = Depends(get_db)):
    
    return create_category(db,category)


@router.delete("/delete",response_model=dict)
def delete(category_id:int, db:Session = Depends(get_db)):
    return delete_category(db, category_id)


@router.put("/update", response_model=dict)
def update(category_id: int, category_data: CategoryUpdate, db: Session = Depends(get_db)):
    return update_category(db, category_id, category_data)

@router.get("/all category", response_model=List[CategoryResponse])
def list_category(db: Session = Depends(get_db)):
    return get_all_categories(db)
