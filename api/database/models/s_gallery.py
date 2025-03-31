from sqlalchemy import Column, Integer, String
from api.database.connection import Base

class GalleryImage(Base):
    __tablename__ = "school_gallery"

    id = Column(Integer, primary_key=True, index=True)
    image_class = Column(String(100), nullable=False)  # e.g., "Sports", "Annual Day"
    image = Column(String(255), nullable=False)  # URL or file path of the image
