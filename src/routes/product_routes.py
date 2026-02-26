from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from db.db import get_session
from schemas.product_schemas import (
    ProductCreateSchema,
    ProductResponseSchema,
    ProductUpdateSchema,
)
from services import product_service

products_router = APIRouter(tags=["Products Routes"])


@products_router.get("/")
def get_all_products(session: Session = Depends(get_session)):
    return product_service.get_all_products(session)


@products_router.get("/{product_id}")
def get_product_by_id(product_id: int, session: Session = Depends(get_session)):
    return product_service.get_product_by_id(session, product_id)


@products_router.put("/{product_id}", response_model=ProductResponseSchema)
def update_product(
    payload: ProductUpdateSchema,
    product_id: int,
    session: Session = Depends(get_session),
):
    return product_service.update_product(session, product_id, payload)


@products_router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int, session: Session = Depends(get_session)):
    return product_service.delete_product(session, product_id)


@products_router.post(
    "/", response_model=ProductResponseSchema, status_code=status.HTTP_201_CREATED
)
def create_product(
    payload: ProductCreateSchema, session: Session = Depends(get_session)
):
    return product_service.create_product(session, payload)
