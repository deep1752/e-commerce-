from sqlalchemy import Column, Integer, String, Enum, DateTime, func
from api.database.connection import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    firstName = Column(String(100), nullable=False)
    middleName = Column(String(100), nullable=True)
    lastName = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    address1 = Column(String(255), nullable=False)
    address2 = Column(String(255), nullable=True)
    address3 = Column(String(255), nullable=True)
    country = Column(String(100), nullable=False)
    state = Column(String(100), nullable=False)
    city = Column(String(100), nullable=False)
    zip = Column(String(100), nullable=False)
    number = Column(String(100), unique=True, nullable=False)
    alternateNumber = Column(String(100),  nullable=True)
    alternateEmail = Column(String(255), index=True, nullable=False)
  
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)

    # Relationship with Address model
    addresses = relationship("Address", back_populates="user", cascade="all, delete-orphan")
    # Relationship with Cart
    cart_items = relationship("Cart", back_populates="user", cascade="all, delete-orphan")
    # Relationship with Review
    reviews = relationship("Review", back_populates="user", cascade="all, delete-orphan")
    # Relationship with Order
    orders = relationship("Order", back_populates="user", cascade="all, delete-orphan")
