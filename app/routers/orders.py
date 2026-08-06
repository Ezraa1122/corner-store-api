from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.order import OrderCreate, OrderOut
from app.services import order_service
from app.core.exceptions import ProductNotFoundError, InsufficientStockError

router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("/", response_model=OrderOut, status_code=201)
def create_order(order_data: OrderCreate, db: Session = Depends(get_db)):
    try:
        return order_service.create_order(db, order_data)
    except ProductNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except InsufficientStockError as e:
        raise HTTPException(status_code=409, detail=str(e))

    