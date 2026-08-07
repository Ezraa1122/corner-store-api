import pytest
from app.services import order_service, product_service
from app.schemas.order import OrderCreate, OrderItemCreate
from app.schemas.product import ProductCreate
from app.core.exceptions import InsufficientStockError

def test_create_order_succeeds_with_enough_stock(db_session):
    product = product_service.create_product(
        db_session, ProductCreate(name="Coffee", price=4.5, stock=10)
    )
    order_data = OrderCreate(
        customer_id=1,
        items=[OrderItemCreate(product_id=product.id, quantity=2)]
    )

    order = order_service.create_order(db_session, order_data)

    assert order.id is not None
    assert order.items[0].quantity == 2

def test_create_order_fails_with_insufficient_stock(db_session):
    product = product_service.create_product(
        db_session, ProductCreate(name="Coffee", price=4.5, stock=1)
    )
    order_data = OrderCreate(
        customer_id=1,
        items=[OrderItemCreate(product_id=product.id, quantity=999)]
    )

    with pytest.raises(InsufficientStockError):
        order_service.create_order(db_session, order_data)

def test_stock_is_decremented_after_order(db_session):
    product = product_service.create_product(
        db_session, ProductCreate(name="Coffee", price=4.5, stock=10)
    )
    order_data = OrderCreate(
        customer_id=1,
        items=[OrderItemCreate(product_id=product.id, quantity=3)]
    )

    order_service.create_order(db_session, order_data)

    db_session.refresh(product)
    assert product.stock == 7
    