from sqlalchemy.orm import Session
from api.database.models.s_user import S_User, Status
from api.database.schemas.s_user import S_UserCreate

# Function to create a new user in the database
def create_user(db: Session, student: S_UserCreate):
    """Create a new user and ensure email uniqueness."""
    existing_email = db.query(S_User).filter(S_User.email == student.email).first()
    if existing_email:
        return "email_exists"

    db_user = S_User(
        first_name=student.first_name,
        last_name=student.last_name,
        fathers_name=student.fathers_name,
        mothers_name=student.mothers_name,
        mobile_number=student.mobile_number,
        email=student.email,
        apply_for=student.apply_for,
        address=student.address,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Get user status by registration number
def get_status_by_registration_number(db: Session, registration_number: str):
    user = db.query(S_User.status).filter(S_User.registration_number == registration_number).first()
    return user.status if user else None

# Get registration number by mobile number
def get_registration_number_by_mobile(db: Session, mobile_number: str):
    user = db.query(S_User.registration_number).filter(S_User.mobile_number == mobile_number).first()
    return user.registration_number if user else None

# Get user by mobile number
def get_user_by_mobile(db: Session, mobile_number: str):
    return db.query(S_User).filter(S_User.mobile_number == mobile_number).first()

# Update status by registration number
def update_status_by_registration_number(db: Session, registration_number: str, new_status: str):
    """Update user status while ensuring it is valid."""
    user = db.query(S_User).filter(S_User.registration_number == registration_number).first()

    if not user:
        return None  # User not found

    if new_status not in {status.value for status in Status}:
        return "invalid_status"  # Invalid status

    user.status = new_status
    db.commit()
    db.refresh(user)
    return user
