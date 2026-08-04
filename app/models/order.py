from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.database import Base
from app.models.product import Product

class Order(Base):
    __tablename__ = "orders"

    id : Mapped[int] = mapped_column(primary_key=True, index=True)
    customer_id : Mapped[int] = mapped_column(ForeignKey("customers.id"))
    status : Mapped[str] = mapped_column(default="pending")
    created_at : Mapped[datetime] = mapped_column(default=datetime.utcnow)

    customer = relationship("Customer")
    items : Mapped[list["OrderItem"]] =relationship(back_populates="order")

class OrderItem(Base):
    __tablename__ = "order_items"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    quantity: Mapped[int]

    order = relationship("Order", back_populates="items")
    product: Mapped["Product"] = relationship()