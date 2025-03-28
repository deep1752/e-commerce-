from pydantic import BaseModel, EmailStr, field_validator
from datetime import datetime
from enum import Enum
from typing import Optional

# Define Enum for Role
class UserRole(str, Enum):
    customer = "customer"
    admin = "admin"

class UserCreate(BaseModel):
    firstName: str
    middleName: Optional[str] = None
    lastName: str
    email: EmailStr
    confirmEmail: EmailStr
    password: str
    confirmPassword: str
    address1: str
    address2: Optional[str] = None
    address3: Optional[str] = None
    country: str
    state: str
    city: str
    zip: str
    number: str
    alternateNumber: Optional[str] = None
    alternateEmail: Optional[str] = None


 

    @field_validator("confirmEmail")
    @classmethod
    def email_must_match(cls, confirmEmail, info):
        if confirmEmail != info.data.get("email"):
            raise ValueError("Emails do not match")
        return confirmEmail

    @field_validator("confirmPassword")
    @classmethod
    def password_must_match(cls, confirmPassword, info):
        if confirmPassword != info.data.get("password"):
            raise ValueError("Passwords do not match")
        return confirmPassword

# Response model (excluding sensitive data)
class UserResponse(BaseModel):
    id: int
    firstName: str
    middleName: Optional[str] = None
    lastName: str
    address1: str
    address2: Optional[str] = None
    address3: Optional[str] = None
    country: str
    state: str
    city: str
    zip: str
    number: str
    alternateNumber: Optional[str] = None
    alternateEmail: Optional[str] = None


    class Config:
        from_attributes = True
   

class UserProfileUpdate(BaseModel):

    firstName: str
    middleName: Optional[str] = None
    lastName: str
    address1: str
    address2: Optional[str] = None
    address3: Optional[str] = None
    country: str
    state: str
    city: str
    zip: str
    number: str
    alternateNumber: Optional[str] = None
    alternateEmail: Optional[str] = None
 
    

    # Pydantic schema for password update
class UserPasswordUpdate(BaseModel):
 
    new_password: str
    confirm_password: str

    
    class Config:
        from_attributes = True

# User login schema
class UserLogin(BaseModel):
    email: EmailStr
    
    password: str
