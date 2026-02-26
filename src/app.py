from fastapi import FastAPI
import uvicorn

from routes import users_routes, product_routes

"""
from db.db import Base, engine
from models import Order, Product, User
"""

app = FastAPI(
    title="Kadituxi Store API",
    description="Kadituxi Store - API for orders management.",
    version="1.0",
)

app.include_router(router=users_routes.users_router, prefix="/users")
app.include_router(router=product_routes.products_router, prefix="/products")

if __name__ == "__main__":
    # Base.metadata.create_all(engine)
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
