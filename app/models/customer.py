from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class Customer(Base):
    __tablename__ = "customers"

    id : Mapped[int] = mapped_column(primary_key=True, index=True)
    name : Mapped[str]
    email : Mapped[str] = mapped_column(unique=True)
