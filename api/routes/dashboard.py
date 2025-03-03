from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.database.connection import get_db
from api.crud.dashboard import get_latest_orders, get_last_month_revenue, get_last_three_months_revenue, get_pending_orders, get_all_delivered_orders

router = APIRouter()
@router.get("/analytics")
def dashboard_analytics(db: Session = Depends(get_db)):
    
    analytics_data = {
        
        "last_month_revenue": get_last_month_revenue(db),
        "last_3_months_revenue": get_last_three_months_revenue(db),
        "latest_5_orders": get_latest_orders(db),
        "pending_orders": get_pending_orders(db),
        "delivered_products": get_all_delivered_orders(db)
    }
    
    return analytics_data