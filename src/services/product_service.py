from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from repositories import product_repository
from schemas.product_schemas import ProductCreateSchema, ProductUpdateSchema


def get_all_products(session: Session):
    return product_repository.get_all_products(session)


def create_product(session: Session, payload: ProductCreateSchema):
    return product_repository.create_product(session, payload)


def get_product_by_id(session: Session, product_id: int):
    product = product_repository.get_product_by_id(session, product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Producto não encontrado"
        )
    return product


def delete_product(session: Session, product_id: int):
    product = get_product_by_id(session, product_id)
    product_repository.delete_product(session, product)


def update_product(session: Session, product_id: int, payload: ProductUpdateSchema):
    product = get_product_by_id(session, product_id)
    return product_repository.update_product(session, product, payload)
