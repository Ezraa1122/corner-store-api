from sqlalchemy.orm import Session
from app.repositories import product_repository
from app.schemas.product import ProductCreate
from app.core.exceptions import ProductNotFoundError
from app.models.product import Product

def get_product_or_false(db: Session, product_id: int) -> Product:
    product = product_repository.get_product(db, product_id)
    if product is None:
        raise ProductNotFoundError(product_id)
    return product

def create_product(db: Session, product_data: ProductCreate) -> Product:
    return product_repository.create_product(db, product_data)

def list_products(db: Session) -> list[Product]:
    return product_repository.list_products(db)
