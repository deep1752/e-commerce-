from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional

from enum import Enum


# Define Enum for Role
class UserRole(str, Enum):
    customer = "customer"
    admin = "admin"

class UserCreate(BaseModel):

    productRequested: str
    quantity: int
    framingSize: Optional[str]
    framingQuantity: Optional[int]
    certifiedCopy: Optional[str]
    certifiedCopyQuantity: Optional[int]
    lastNameBeforeMarriage: str
    secondGivenName: Optional[str]
    lastNameAtBirth: str
    sex: str
    marriageDate: date
    streetAddress: str
    streetAddress2: Optional[str]
    city: str
    region: str
    postalCode: str
    marriageRegNumber: str

# Response model (excluding sensitive data)
class UserResponse(BaseModel):


    id: int
    productRequested: str
    quantity: int
    framingSize: Optional[str]
    framingQuantity: Optional[int]
    certifiedCopy: Optional[str]
    certifiedCopyQuantity: Optional[int]
    lastNameBeforeMarriage: str
    secondGivenName: Optional[str]
    lastNameAtBirth: str
    sex: str
    marriageDate: date
    streetAddress: str
    streetAddress2: Optional[str]
    city: str
    region: str
    postalCode: str
    marriageRegNumber: str
   

class UserProfileUpdate(BaseModel):

    productRequested: str
    quantity: int
    framingSize: Optional[str]
    framingQuantity: Optional[int]
    certifiedCopy: Optional[str]
    certifiedCopyQuantity: Optional[int]
    lastNameBeforeMarriage: str
    secondGivenName: Optional[str]
    lastNameAtBirth: str
    sex: str
    marriageDate: date
    streetAddress: str
    streetAddress2: Optional[str]
    city: str
    region: str
    postalCode: str
    marriageRegNumber: str

  
    
    class Config:
        from_attributes = True
