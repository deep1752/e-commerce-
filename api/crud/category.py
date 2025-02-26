from sqlalchemy.orm import Session
from fastapi import HTTPException
from api.database.models.category import Category
from api.database.schemas.category import CategoryCreate, CategoryUpdate

def create_category(db: Session,  category: CategoryCreate):
    
    db_category = Category(

        name = category.name,
        created_at = category.created_at,
        updated_at = category.updated_at

        

    )
    db.add(db_category)  # Add the user to the database session
    db.commit()  # Commit the transaction to save changes
    db.refresh(db_category)  # Refresh the user instance with the latest data from DB
    return db_category


def delete_category(db:Session, category_id:int):
    category = db.query(Category).filter(Category.id == category_id). first()
    if category:
        db.delete(category)
        db.commit()
        return {"success": True, "message":"category deleted successfully"}
    return {"success":False,"message":"category not found"}


def update_category(db: Session, category_id: int,category_data: CategoryUpdate):
    # Fetch product from the database (Product is the SQLAlchemy model)
    category = db.query(Category).filter(Category.id == category_id).first()

    if not category:
        raise HTTPException(status_code=404, detail="category not found")

# #    Update only provided fields
    category_data_dict = category_data.model_dump(exclude_unset=True)  # Use model_dump() for Pydantic v2

    for key, value in category_data_dict.items():
        setattr(category, key, value)

    db.commit()
    db.refresh(category)

    return {"message": "category updated successfully"}

def get_all_categories(db:Session):

    return db.query(Category).all()