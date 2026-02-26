from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from db.db import get_session
from schemas.users_schemas import (
    LoginUserSchema,
    ResponseUserSchema,
    RegisterUserSchema,
    TokenSchema,
)
from services import user_service

users_router = APIRouter(tags=["Users Routes"])


@users_router.post(
    "/auth/register",
    response_model=ResponseUserSchema,
    status_code=status.HTTP_201_CREATED,
)
async def register_user(
    user_payload: RegisterUserSchema, session: Session = Depends(get_session)
):
    return user_service.register_user(user_payload, session)


@users_router.post("/auth/login", response_model=TokenSchema)
def login_user(user_payload: LoginUserSchema, session: Session = Depends(get_session)):
    return user_service.login_user(user_payload, session)


@users_router.post("/auth/get-user", response_model=ResponseUserSchema)
def get_user(token_payload: TokenSchema, session: Session = Depends(get_session)):
    return user_service.get_user(token_payload.access_token, session)
