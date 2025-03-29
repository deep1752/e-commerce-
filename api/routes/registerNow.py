from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from api.database.connection import get_db
from api.database.schemas.registerNow import UserCreate, UserResponse
from api.crud.registerNow import create_user, get_user_by_email,get_user_by_id
from fastapi.security import OAuth2PasswordBearer
from api.token import get_current_user

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = create_user(db, user)

    return JSONResponse(
        status_code=201,
        content={
            "message": "Registration successful",
        
            
        },
    )



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



