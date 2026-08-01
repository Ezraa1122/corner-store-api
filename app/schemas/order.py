from pydantic import BaseModel, ConfigDict
from typing import List
from app.schemas.product import ProductOut

class OrderItemCreate(BaseModel):
    product_id : int
    quantity :int

class OrderCreate(BaseModel):
    customer_id : int
    items : List[OrderItemCreate]

class OrderItemOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    quantity : int
    product: ProductOut

class OrderOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id : int
    customer_id : int
    status : str
    items : List[OrderItemOut]
