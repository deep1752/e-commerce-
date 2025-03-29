from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, File, UploadFile, Form
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
import os
import shutil
from api.database.connection import get_db
from api.database.schemas.marriage import UserCreate, UserResponse
from api.crud.marriage import create_user
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)  # Ensure the upload folder exists

@router.post("/register", response_model=UserResponse)
async def register(
    productRequested: str = Form(...),
    quantity: int = Form(...),
    framingSize: str = Form(...),
    framingQuantity: int = Form(...),
    certifiedCopy: UploadFile = File(...),
    certifiedCopyQuantity: int = Form(...),
    lastNameBeforeMarriage: str = Form(...),
    secondGivenName: str = Form(None),
    lastNameAtBirth: str = Form(...),
    sex: str = Form(...),
    marriageDate: str = Form(...),  # Received as string
    streetAddress: str = Form(...),
    streetAddress2: str = Form(None),
    city: str = Form(...),
    region: str = Form(...),
    postalCode: str = Form(...),
    marriageRegNumber: str = Form(...),
    db: Session = Depends(get_db)
):
    try:
        marriageDate = datetime.strptime(marriageDate, "%Y-%m-%d").date()  # Convert to date
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD.")

    # Save uploaded file
    file_location = f"{UPLOAD_DIR}/{certifiedCopy.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(certifiedCopy.file, buffer)

    # Create user object with file path instead of file
    user_data = {
        "productRequested": productRequested,
        "quantity": quantity,
        "framingSize": framingSize,
        "framingQuantity": framingQuantity,
        "certifiedCopy": file_location,  # Store file path in DB
        "certifiedCopyQuantity": certifiedCopyQuantity,
        "lastNameBeforeMarriage": lastNameBeforeMarriage,
        "secondGivenName": secondGivenName,
        "lastNameAtBirth": lastNameAtBirth,
        "sex": sex,
        "marriageDate": marriageDate,  # Now correctly formatted
        "streetAddress": streetAddress,
        "streetAddress2": streetAddress2,
        "city": city,
        "region": region,
        "postalCode": postalCode,
        "marriageRegNumber": marriageRegNumber,
    }

    new_user = create_user(db, UserCreate(**user_data))

    return JSONResponse(
        status_code=201,
        content={
            "message": "Registration successful",
            "user_id": new_user.id,
            "marriage_reg_number": new_user.marriageRegNumber,
            "file_path": new_user.certifiedCopy  # Return file path
        },
    )
