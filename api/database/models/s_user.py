from sqlalchemy import Column, Integer, String, Enum as SQLEnum, DateTime, func
from api.database.connection import Base
from enum import Enum as PyEnum
import random
import string

# Define ApplyFor Enum Correctly
class ApplyFor(str, PyEnum):
    nursery = "Nursery/Pre-Nursery"
    lkg = "LKG (Lower Kindergarten)"
    ukg = "UKG (Upper Kindergarten)"
    first = "1st"
    second = "2nd"
    third = "3rd"
    fourth = "4th"
    sixth = "6th"
    seventh = "7th"
    eighth = "8th"
    ninth = "9th"
    tenth = "10th"  # ✅ Added 10th class
    eleventh = "11th"
    twelfth = "12th"

# Define Status Enum Correctly
class Status(str, PyEnum):
    pending = "pending"
    processing = "in processing"
    completed = "completed"
    rejected = "rejected"

# Function to Generate Registration Number
def generate_registration_number():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

# Define the SQLAlchemy Model
class S_User(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    fathers_name = Column(String(100), nullable=False)
    mothers_name = Column(String(100), nullable=False)
    mobile_number = Column(String(100), unique=True, nullable=False)
    email = Column(String(255), index=True, nullable=False)
    apply_for = Column(SQLEnum(ApplyFor, values_callable=lambda x: [e.value for e in x]), nullable=False)
    address = Column(String(255), nullable=False)
    status = Column(SQLEnum(Status, values_callable=lambda x: [e.value for e in x]), default=Status.pending.value, nullable=False)
    registration_number = Column(String(20), unique=True, nullable=False, default=lambda: generate_registration_number())
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)
