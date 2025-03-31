from pydantic import BaseModel, EmailStr

from enum import Enum

from api.database.models.s_user import ApplyFor ,Status
# Define Enum for Role
class UserRole(str, Enum):
    customer = "customer"
    admin = "admin"

class S_UserCreate(BaseModel):
    first_name: str
    last_name: str
    fathers_name: str
    mothers_name: str
    mobile_number: str
    email: EmailStr
    apply_for: ApplyFor
    address: str

 
# Response model (excluding sensitive data)
class S_UserResponse(BaseModel):
    registration_number: str
    

    class Config:
        from_attributes = True
   

class S_UserProfileUpdate(BaseModel):

    first_name: str
    last_name: str
    fathers_name: str
    mothers_name: str
    mobile_number: str
    email: EmailStr
    apply_for: ApplyFor
    address: str
   
