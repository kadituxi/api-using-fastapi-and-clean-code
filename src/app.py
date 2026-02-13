from fastapi import FastAPI
import uvicorn

from routes import users_routes

"""
from db.db import Base, engine
from models.order_model import Order
from models.product_model import Product
from models.user_model import User
"""


app = FastAPI(
    title="Kadituxe Store API",
    description="Kadituxe Store - API for orders management.",
    version="1.0",
)

app.include_router(router=users_routes.users_router, prefix="/users")

if __name__ == "__main__":
    # Base.metadata.create_all(engine)
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
