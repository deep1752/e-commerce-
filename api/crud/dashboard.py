from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from sqlalchemy import func
from api.database.models.order import Order


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