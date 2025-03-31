from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.database.connection import get_db
from api.database.schemas.s_user import S_UserCreate, S_UserResponse
from api.crud.s_user import (
    create_user,
    get_status_by_registration_number,
    get_registration_number_by_mobile,
    get_user_by_mobile,
    update_status_by_registration_number,
)
from api.database.models.s_user import Status

router = APIRouter()

# Register a new user
@router.post("/register", response_model=S_UserResponse)
def register(user: S_UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_mobile(db, user.mobile_number)
    if existing_user:
        raise HTTPException(status_code=400, detail="Mobile number already registered")
    
    new_user = create_user(db, user)
    if new_user == "email_exists":
        raise HTTPException(status_code=400, detail="Email already registered")

    if not new_user:
        raise HTTPException(status_code=500, detail="User registration failed")

    return new_user

# Get user status by registration number
@router.get("/status/{registration_number}")
def get_status(registration_number: str, db: Session = Depends(get_db)):
    status = get_status_by_registration_number(db, registration_number)
    if not status:
        raise HTTPException(status_code=404, detail="Registration number not found")
    return {"registration_number": registration_number, "status": status}

# Get registration number by mobile number
@router.get("/registration/{mobile_number}")
def get_registration(mobile_number: str, db: Session = Depends(get_db)):
    registration_number = get_registration_number_by_mobile(db, mobile_number)
    if not registration_number:
        raise HTTPException(status_code=404, detail="Mobile number not found")
    return {"mobile_number": mobile_number, "registration_number": registration_number}

# Update user status by registration number
@router.put("/update-status/{registration_number}")
def update_status(registration_number: str, new_status: str, db: Session = Depends(get_db)):
    if new_status not in {status.value for status in Status}:
        raise HTTPException(status_code=400, detail="Invalid status value. Choose from: pending, processing, completed, rejected.")

    updated_user = update_status_by_registration_number(db, registration_number, new_status)

    if updated_user is None:
        raise HTTPException(status_code=404, detail="Registration number not found")

    return {"registration_number": updated_user.registration_number, "status": updated_user.status}
