from fastapi import APIRouter, Depends
from api.database.schemas.user import UserResponse, UserProfileUpdate, UserPasswordUpdate
from api.token import get_current_user
from api.database.connection import get_db
from sqlalchemy.orm import Session
from api.crud.user import update_user_profile , update_user_password, get_user_by_email,delete_user,get_user_by_id
from fastapi import HTTPException

# Creating an API router instance for handling user-related routes
router = APIRouter()

@router.get("/profile", response_model=UserResponse)
def get_profile(current_user: UserResponse = Depends(get_current_user)):

    return current_user


@router.get("/profile/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    """Retrieve a user by their ID."""
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return UserResponse.model_validate(user)  # Convert SQLAlchemy model to Pydantic schema



@router.put("/profile /", response_model=dict)
def update(user_id: int, user_data: UserProfileUpdate, db: Session = Depends(get_db)):
    return update_user_profile(db, user_id, user_data)


@router.put("/profile")
def update_password(
    email: str, 
    password_data: UserPasswordUpdate, 
    db: Session = Depends(get_db)
):
    """API endpoint to update a user's password."""
    user = get_user_by_email(db, email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if password_data.new_password != password_data.confirm_password:
        raise HTTPException(status_code=400, detail="New password and confirmation password do not match")

    # Update password directly
    update_user_password(db, user, password_data.new_password)
    
    return {"message": "Password updated successfully"}

@router.delete("/profile", response_model=dict)
def delete(email: str, password: str, db: Session = Depends(get_db)):
    return delete_user(db, email, password)
