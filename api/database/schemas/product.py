from pydantic import BaseModel
from datetime import datetime
from typing import Literal
from api.database.schemas.category import CategoryBase

# User creation schema
class ProductCreate(BaseModel):

    category_id : int 
    name : str 
    description : str 
    status: Literal["Active", "Inactive"]
    mrp : float
    net_price : float
    quantity_in_stock : int 
    image : str 
# Response model (excluding sensitive data)
class ProductResponse(BaseModel):

    name : str 
    category : CategoryBase
    description : str 
    status: Literal["Active", "Inactive"]
    mrp : float
    net_price : float
    quantity_in_stock : int 
    image : str 
    created_at : datetime
    updated_at : datetime

class ProductUpdate(BaseModel):

    category_id : int 
    
    name : str 
    description : str 
    mrp : float
    net_price : float
    quantity_in_stock : int 
    image : str 
    updated_at : datetime
    
    class Config:
        from_attributes = True



