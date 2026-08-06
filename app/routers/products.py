from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.product import ProductCreate, ProductOut
from app.services import product_service
from app.core.exceptions import ProductNotFoundError

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/", response_model=list[ProductOut])
def list_products(db: Session = Depends(get_db)):
    return product_service.list_products(db)

@router.post("/", response_model=ProductOut, status_code=201)
def create_product(product_data: ProductCreate, db: Session = Depends(get_db)):
    return product_service.create_product(db, product_data)

@router.get("/{product_id}", response_model=ProductOut)
def get_product(product_id: int, db: Session = Depends(get_db)):
    try:
        return product_service.get_product_or_false(db, product_id)
    except ProductNotFoundError:
        raise HTTPException(status_code=404, detail="Product not found")
    