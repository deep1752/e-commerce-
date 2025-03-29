from pydantic import BaseModel, EmailStr

from enum import Enum


# Define Enum for Role
class UserRole(str, Enum):
    customer = "customer"
    admin = "admin"

class UserCreate(BaseModel):
    firstName: str
    lastName: str
    email: EmailStr
    phoneNumber: str
    streetAddress: str
    streetAddress2: str = None
    state: str
    country: str
    postalCode: str
    areaCode: str
    termsAccepted: bool

 

# Response model (excluding sensitive data)
class UserResponse(BaseModel):
    id: int
    firstName: str
    lastName: str
    streetAddress: str
    streetAddress2: str = None
    state: str
    country: str
    postalCode: str
    areaCode: str
    termsAccepted: bool
    class Config:
        from_attributes = True
   

class UserProfileUpdate(BaseModel):

    firstName: str
    lastName: str
    streetAddress: str
    streetAddress2: str = None
    state: str
    country: str
    postalCode: str
    areaCode: str
    termsAccepted: bool
    

  
    
    class Config:
        from_attributes = True
