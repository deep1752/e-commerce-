from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, joinedload
from api.database.connection import get_db
from api.database.schemas.product import ProductResponse, ProductCreate, ProductUpdate
from api.database.models.product import Product
from api.crud.product import create_product, delete_product, update_product, get_all_products, get_active_products
from typing import List
from datetime import datetime

# Creating an API router instance for handling product-related routes
router = APIRouter()

@router.post("/add", response_model=ProductResponse)
def add_product(product: ProductCreate, db: Session = Depends(get_db)):
    """
    Add a new product to the database.
    """
    return create_product(db, product)

@router.delete("/delete", response_model=dict)
def delete_product_by_id(product_id: int, db: Session = Depends(get_db)):
    """
    Delete a product by its ID.
    """
    return delete_product(db, product_id)

@router.put("/update", response_model=dict)
def update_product_by_id(product_id: int, product_data: ProductUpdate, db: Session = Depends(get_db)):
    """
    Update product details.
    """
    return update_product(db, product_id, product_data)

@router.get("/products", response_model=List[ProductResponse])
def get_all_products_list(db: Session = Depends(get_db)):
    """
    Retrieve all products from the database.
    """
    return db.query(Product).options(joinedload(Product.category)).all()
@router.post("/add", response_model=ProductResponse)
def add(product: ProductCreate, db: Session = Depends(get_db)):
    # ✅ Ensure timestamps are set automatically
    product.created_at = datetime.utcnow()
    product.updated_at = datetime.utcnow()
    
    return create_product(db, product)

@router.get("/active", response_model=List[ProductResponse])
def get_active_products_list(db: Session = Depends(get_db)):
    """
    Retrieve all active products.
    """
    return get_active_products(db)
