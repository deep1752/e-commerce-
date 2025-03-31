from pydantic import BaseModel, HttpUrl
from typing import List

# Base schema
class GalleryImageBase(BaseModel):
    image_class: str
    image: HttpUrl  # Ensures it's a valid URL

# Schema for Creating a Gallery Image
class GalleryImageCreate(GalleryImageBase):
    pass

# Schema for Reading a Gallery Image
class GalleryImageResponse(GalleryImageBase):
    id: int

    class Config:
        from_attributes = True

# Schema for List Response
class GalleryImageListResponse(BaseModel):
    images: List[GalleryImageResponse]
