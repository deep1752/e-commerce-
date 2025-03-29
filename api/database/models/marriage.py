
from api.database.connection import Base
from sqlalchemy import  Column, Integer, String, Date, Enum

class MarriageForm(Base):
    __tablename__ = "marriage"

    
    id = Column(Integer, primary_key=True, index=True)
    productRequested = Column(String(255), index=True)
    quantity = Column(Integer)
    framingSize = Column(String(255))
    framingQuantity = Column(Integer)
    certifiedCopy = Column(String(255), nullable=True)
    certifiedCopyQuantity = Column(Integer)
    lastNameBeforeMarriage = Column(String(255))
    secondGivenName = Column(String(255), nullable=True)
    lastNameAtBirth = Column(String(255))
    sex = Column(Enum("Male", "Female", "Other", name="sex_enum"))
    marriageDate = Column(Date)
    streetAddress = Column(String(255))
    streetAddress2 = Column(String(255), nullable=True)
    city = Column(String(255))
    region = Column(String(255))
    postalCode = Column(String(255))
    marriageRegNumber = Column(String(255), unique=True)
