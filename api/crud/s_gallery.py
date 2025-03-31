from sqlalchemy.orm import Session
from api.database.models.s_gallery import GalleryImage
from api.database.schemas.s_gallery import GalleryImageCreate

# Create a new gallery image
def create_gallery_image(db: Session, image_data: GalleryImageCreate):
    db_image = GalleryImage(**image_data.model_dump())
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image

# Get all images
def get_all_gallery_images(db: Session):
    return db.query(GalleryImage).all()

# Get an image by ID
def get_gallery_image_by_id(db: Session, image_id: int):
    return db.query(GalleryImage).filter(GalleryImage.id == image_id).first()

# Delete an image by ID
def delete_gallery_image(db: Session, image_id: int):
    db_image = get_gallery_image_by_id(db, image_id)
    if db_image:
        db.delete(db_image)
        db.commit()
        return True
    return False
