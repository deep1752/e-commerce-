from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from api.database.connection import get_db
from api.database.schemas.order import OrderResponse,OrderCreate
from api.crud.order import create_order,get_all_orders

# Creating an API router instance for handling user-related routes
router = APIRouter()

@router.post("/add", response_model=OrderResponse)
def add(order: OrderCreate , db:Session = Depends(get_db)):
    
    return create_order(db,order)


@router.get("/all_order", response_model=List[OrderResponse])
def list_order(db: Session = Depends(get_db)):
    return get_all_orders(db)


