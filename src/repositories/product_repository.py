from sqlalchemy import select
from sqlalchemy.orm import Session

from models.product_model import Product
from schemas.product_schemas import ProductCreateSchema, ProductUpdateSchema


def get_all_products(session: Session) -> list[Product]:
    products = session.execute(select(Product)).scalars().all()
    return products


def create_product(session: Session, payload: ProductCreateSchema) -> Product:
    product = Product(**payload.model_dump())
    session.add(product)
    session.commit()
    session.refresh(product)
    return product


def get_product_by_id(session: Session, product_id: int):
    return session.execute(
        select(Product).where(Product.id == product_id)
    ).scalar_one_or_none()


def delete_product(session: Session, product: Product):
    session.delete(product)
    session.commit()


def update_product(session: Session, product: Product, payload: ProductUpdateSchema):
    for k, v in payload.model_dump().items():
        if v:
            setattr(product, f"{k}", v)
    session.commit()
    session.refresh(product)
    return product
