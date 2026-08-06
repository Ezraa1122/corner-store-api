from sqlalchemy.orm import Session
from app.repositories import order_repository
from app.repositories import product_repository
from app.services import product_service
from app.schemas.order import OrderCreate
from app.core.exceptions import InsufficientStockError
from app.models.order import Order

def create_order(db: Session, order_data: OrderCreate) -> Order:
    #validate before writing into database
    validated_items = []
    for item in order_data.items:
        product = product_service.get_product_or_false(db, item.product_id)
        if product.stock < item.quantity:
            raise InsufficientStockError(
                product_id=product.id,
                requested=item.quantity,
                available=product.stock
            )
        validated_items.append({"product_id": product.id, "quantity": item.quantity})

    #after everything checks out, create the order
    order = order_repository.create_order(
        db,
        customer_id=order_data.customer_id,
        items=validated_items
    )

    #decrement stock for each product
    for item in validated_items:
        product_repository.decrement_stock(db, item["product_id"], item["quantity"])

    return order