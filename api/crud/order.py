from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from sqlalchemy import func
from api.database.models.order import Order
from api.database.schemas.order import OrderCreate

def create_order(db: Session,  order: OrderCreate):
    
    db_order = Order(


        user_id = order.user_id,
        subtotal = order.subtotal,
        discount = order.discount,
        total = order.total,
        status = order.status,
        shipping_address = order.shipping_address,
        created_at = order.created_at,
        updated_at = order.updated_at
    )
    db.add(db_order)  # Add the user to the database session
    db.commit()  # Commit the transaction to save changes
    db.refresh(db_order)  # Refresh the user instance with the latest data from DB
    return db_order


def get_latest_orders(db: Session, limit: int = 5):
    return db.query(Order).order_by(Order.created_at.desc()).limit(limit).all()

def get_last_month_revenue(db: Session):
    last_month_start = datetime.now().replace(day=1) - timedelta(days=1)
    last_month_start = last_month_start.replace(day=1)
    last_month_end = last_month_start.replace(day=1) + timedelta(days=31)

    return db.query(func.sum(Order.total)).filter(
        Order.created_at >= last_month_start, Order.created_at < last_month_end
    ).scalar() or 0

def get_last_three_months_revenue(db: Session):
    three_months_ago = datetime.now() - timedelta(days=90)
    return db.query(func.sum(Order.total)).filter(Order.created_at >= three_months_ago).scalar() or 0

def get_pending_orders(db: Session):
    return db.query(Order).filter(Order.status == "pending").all()

def get_all_delivered_orders(db: Session):
    return db.query(Order).filter(Order.status == "delivered").all()

def get_all_orders(db:Session):

    return db.query(Order).all()