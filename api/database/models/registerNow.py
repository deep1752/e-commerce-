from sqlalchemy import Column, Integer, String,Boolean
from api.database.connection import Base
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr


class RegisterNow (Base):
    __tablename__ = "registernow"

    id = Column(Integer, primary_key=True, index=True)
    firstName = Column(String(255), nullable=False)
    lastName = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    phoneNumber = Column(String(255), unique=True ,nullable=False)
    streetAddress = Column(String(255), nullable=False)
    streetAddress2 = Column(String(255), nullable=True)
    state = Column(String(255), nullable=False)
    country = Column(String(255), nullable=False)
    postalCode = Column(String(255), nullable=False)
    areaCode = Column(String(255), nullable=False)
    termsAccepted = Column(Boolean, default=False, nullable=False)
