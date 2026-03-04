import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime, Float

from db.db import Base


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    description = Column(Text)
    qtd_stock = Column(Integer)
    price = Column(Float)

    created_at = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))
    updated_at = Column(DateTime, onupdate=datetime.datetime.now(datetime.timezone.utc))

    def __repr__(self):
        return f"<Product>: {self.name} | {self.price} kz"
