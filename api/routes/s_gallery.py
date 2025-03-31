from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.database.connection import get_db
from api.database.schemas.s_gallery import GalleryImageCreate, GalleryImageResponse, GalleryImageListResponse
from api.crud.s_gallery import create_gallery_image, get_all_gallery_images, get_gallery_image_by_id, delete_gallery_image

router = APIRouter(prefix="/gallery", tags=["Gallery"])

# Create a new image entry
@router.post("/", response_model=GalleryImageResponse)
def add_gallery_image(image_data: GalleryImageCreate, db: Session = Depends(get_db)):
    return create_gallery_image(db, image_data)

# Get all images
@router.get("/", response_model=GalleryImageListResponse)
def fetch_all_gallery_images(db: Session = Depends(get_db)):
    images = get_all_gallery_images(db)
    return {"images": images}

# Get an image by ID
@router.get("/{image_id}", response_model=GalleryImageResponse)
def fetch_gallery_image(image_id: int, db: Session = Depends(get_db)):
    image = get_gallery_image_by_id(db, image_id)
    if not image:
        raise HTTPException(status_code=404, detail="Image not found")
    return image

# Delete an image
@router.delete("/{image_id}")
def remove_gallery_image(image_id: int, db: Session = Depends(get_db)):
    if not delete_gallery_image(db, image_id):
        raise HTTPException(status_code=404, detail="Image not found")
    return {"message": "Image deleted successfully"}
