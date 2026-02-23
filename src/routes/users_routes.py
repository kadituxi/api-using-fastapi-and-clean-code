from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from db.db import get_session
from schemas.users_schemas import (
    LoginUserSchema,
    ResponseUserSchema,
    RegisterUserSchema,
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


@users_router.post("/auth/login")
def login_user(user_payload: LoginUserSchema, session: Session = Depends(get_session)):
    return user_service.login_user(user_payload, session)
