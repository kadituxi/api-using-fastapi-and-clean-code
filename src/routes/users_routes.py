from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.db import get_session
from repositories import users_repository
from schemas.users_schemas import RegisterUserSchema, LoginUserSchema

users_router = APIRouter(tags=["Users Routes"])


@users_router.post(
    "/auth/register-user",
    response_model=RegisterUserSchema,
    status_code=status.HTTP_201_CREATED,
)
async def register_user(
    user_payload: RegisterUserSchema, session: Session = Depends(get_session)
):
    user = users_repository.get_user_by_email(user_payload.email, session)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Usuário já cadastrado"
        )
    user = users_repository.register_user(user_payload, session)
    return user


@users_router.post("/auth/login")
def login_user(user_payload: LoginUserSchema, session: Session = Depends(get_session)):
    user = users_repository.get_user_by_email(user_payload.email, session)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado"
        )
    if user_payload.password == user.password:
        return {"success": True}
    return {"success": False}
