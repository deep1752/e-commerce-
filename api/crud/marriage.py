from sqlalchemy.orm import Session
from api.database.models.marriage import MarriageForm
from api.database.schemas.marriage import UserCreate
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

def create_user(db: Session, user: UserCreate):
    existing_user = db.query(MarriageForm).filter_by(marriageRegNumber=user.marriageRegNumber).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Marriage Registration Number already exists")
    
    new_user = MarriageForm(
        productRequested=user.productRequested,
        quantity=user.quantity,
        framingSize=user.framingSize,
        framingQuantity=user.framingQuantity,
        certifiedCopy=user.certifiedCopy,  # Store file path
        certifiedCopyQuantity=user.certifiedCopyQuantity,
        lastNameBeforeMarriage=user.lastNameBeforeMarriage,
        secondGivenName=user.secondGivenName,
        lastNameAtBirth=user.lastNameAtBirth,
        sex=user.sex,
        marriageDate=user.marriageDate,
        streetAddress=user.streetAddress,
        streetAddress2=user.streetAddress2,
        city=user.city,
        region=user.region,
        postalCode=user.postalCode,
        marriageRegNumber=user.marriageRegNumber,
    )

    db.add(new_user)
    
    try:
        db.commit()
        db.refresh(new_user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Duplicate entry detected")
    
    return new_user
