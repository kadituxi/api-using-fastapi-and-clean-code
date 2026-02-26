from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from schemas.users_schemas import LoginUserSchema, RegisterUserSchema
from repositories import users_repository
from utils.password_hash import generate_password_hash, check_password_hash
from utils.auth import create_access_token, decode_token


def register_user(user_payload: RegisterUserSchema, session: Session):
    user = users_repository.get_user_by_email(user_payload.email, session)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Usuário já cadastrado"
        )
    user_payload.password = generate_password_hash(user_payload.password)
    user = users_repository.register_user(user_payload, session)
    return user


def login_user(user_payload: LoginUserSchema, session: Session):
    user = users_repository.get_user_by_email(user_payload.email, session)
    if not user or not check_password_hash(user_payload.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuário não encontrado ou senha incorrecta",
        )
    token_data = {"sub": user.email}
    token = create_access_token(token_data)
    return {"access_token": token, "token_type": "bearer"}


def get_user(token: str, session: Session):
    token_data = decode_token(token)
    user_email = token_data.get("sub")
    user = users_repository.get_user_by_email(user_email, session)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido ou expirado",
        )
    return user
