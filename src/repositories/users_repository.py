from typing import Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from models.user_model import User
from schemas.users_schemas import RegisterUserSchema


def get_user_by_email(email: str, session: Session) -> Optional[User]:
    user = session.execute(select(User).where(User.email == email)).scalars().first()
    return user


def register_user(payload: RegisterUserSchema, session: Session) -> User:
    user = User(name=payload.name, email=payload.email, password=payload.password)
    session.add(user)
    session.commit()
    return user
