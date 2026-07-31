from pydantic import BaseModel, ConfigDict

class ProductCreate(BaseModel):
    name : str
    price : float
    stock : int

class ProductOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id : int
    name : str
    price : float
    stock : int