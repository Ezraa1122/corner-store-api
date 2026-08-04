from sqlalchemy.orm import Session
from app.models.order import Order, OrderItem

def get_order(db: Session, order_id: int) -> Order | None:
    return db.query(Order).filter(Order.id == order_id).first()

def list_orders(db: Session) -> list[Order]:
    return db.query(Order).all()

def create_order(db: Session, customer_id: int, items: list[dict]) -> Order:
    order = Order(customer_id=customer_id)
    db.add(order)
    db.flush() #assigns order.id without commiting yet

    for item in items:
        order_item = OrderItem(
            order_id=order.id,
            product_id=item["product_id"],
            quantity=item["quantity"]
        )
        db.add(order_item)

    db.commit()
    db.refresh(order)
    return order