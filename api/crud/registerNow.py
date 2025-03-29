from sqlalchemy.orm import Session
from api.database.models.registerNow import RegisterNow
from api.database.schemas.registerNow import UserCreate 


# Function to create a new user in the database
def create_user(db: Session, user: UserCreate):
    
    db_user = RegisterNow(

         
        firstName = user.firstName,
        lastName = user.lastName,
        email = user.email,
        phoneNumber = user.phoneNumber,
        streetAddress = user.streetAddress,
        streetAddress2 = user.streetAddress2,
        state = user.state,
        country = user.country,
        postalCode = user.postalCode,
        areaCode = user.areaCode,
        termsAccepted = user.termsAccepted

  
        
    )
    db.add(db_user)  # Add the user to the database session
    db.commit()  # Commit the transaction to save changes
    db.refresh(db_user)  # Refresh the user instance with the latest data from DB
    return db_user

# Function to retrieve a user by email
def get_user_by_email(db: Session, email: str):
    
    return db.query(RegisterNow).filter(RegisterNow.email == email).first()

# Function to retrieve a user by ID
def get_user_by_id(db: Session, user_id: int):
   
    return db.query(RegisterNow).filter(RegisterNow.id == user_id).first()
