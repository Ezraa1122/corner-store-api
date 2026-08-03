from sqlalchemy.orm import Session
from app.schemas.product import ProductCreate
from app.models.product import Product

def get_product(db: Session, product_id: int) -> Product | None:
    return db.query(Product).filter(Product.id == product_id).first()

def list_products(db: Session) -> list[Product]:
    return db.query(Product).all()

def create_product(db: Session, product_data: ProductCreate) -> Product:
    product = Product(
        name=product_data.name,
        price=product_data.price,
        stock=product_data.stock
    )
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def decrement_stock(db: Session, product_id: int, quantity: int) -> Product | None:
    product = get_product(db, product_id)
    if product is None:
        return None
    product.stock -= quantity
    db.commit()
    db.refresh(product)
    return product
