from fastapi import FastAPI
from app.database import Base, engine
from app.routers import products, orders

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Corner Store API")

app.include_router(products.router)
app.include_router(orders.router)

@app.get("/")
def root():
    return {"status": "ok"}