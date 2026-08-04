from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class Product (Base):
    __tablename__ = "products"

    id : Mapped[int] = mapped_column(primary_key=True, index=True)
    name : Mapped[str]
    price : Mapped[float]
    stock : Mapped[int] = mapped_column(default=0)
    