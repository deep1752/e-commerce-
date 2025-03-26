from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.database.connection import get_db
from api.database.schemas.product import ProductResponse,ProductCreate, ProductUpdate
from api.crud.product import create_product, delete_product,update_product, get_all_products, get_active_products
from typing import List

# Creating an API router instance for handling user-related routes
router = APIRouter()

@router.post("/add", response_model=ProductResponse)
def add(product: ProductCreate , db:Session = Depends(get_db)):
    
    return create_product(db,product)

@router.delete("/delete",response_model=dict)
def delete(product_id:int, db:Session = Depends(get_db)):
    return delete_product(db, product_id)


@router.put("/update", response_model=dict)
def update(product_id: int, product_data: ProductUpdate, db: Session = Depends(get_db)):
    return update_product(db, product_id, product_data)

@router.get("/all_product", response_model=List[ProductResponse])
def list_product(db: Session = Depends(get_db)):
    return get_all_products(db)


# Get all active products
@router.get("/active", response_model=List[ProductResponse])
def get_active(db: Session = Depends(get_db)):
    return get_active_products(db)
