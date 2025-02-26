from sqlalchemy.orm import Session
from api.database.models.user import User
from api.database.schemas.user import UserCreate, UserProfileUpdate ,UserPasswordUpdate
from api.security import hash_password
from fastapi import HTTPException
from api.security import verify_password

# Function to create a new user in the database
def create_user(db: Session, user: UserCreate):
    
    db_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password),  # Hash the password before storing
        mob_number=user.mob_number,
        role = user.role,
        created_at = user.created_at,
        updated_at = user.updated_at

        
    )
    db.add(db_user)  # Add the user to the database session
    db.commit()  # Commit the transaction to save changes
    db.refresh(db_user)  # Refresh the user instance with the latest data from DB
    return db_user

# Function to retrieve a user by email
def get_user_by_email(db: Session, email: str):
    
    return db.query(User).filter(User.email == email).first()

# Function to retrieve a user by ID
def get_user_by_id(db: Session, user_id: int):
   
    return db.query(User).filter(User.id == user_id).first()


def update_user_profile(db: Session, user_id: int, user_data: UserProfileUpdate):
    # Fetch product from the database (Product is the SQLAlchemy model)
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="user not found")

# #    Update only provided fields
    user_data_dict = user_data.model_dump(exclude_unset=True)  # Use model_dump() for Pydantic v2

    for key, value in user_data_dict.items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)

    return {"message": "user updated successfully"}



def update_user_password(db: Session, user: User, new_password: str):
    """Update user's password."""
    user.password = hash_password(new_password)
    db.commit()
    db.refresh(user)
    return user