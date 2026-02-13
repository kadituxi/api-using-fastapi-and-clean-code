from pydantic import BaseModel, EmailStr


class BaseUserSchema(BaseModel):
    name: str
    email: EmailStr


class LoginUserSchema(BaseModel):
    email: EmailStr
    password: str


class RegisterUserSchema(BaseUserSchema):
    password: str


class ResponseUserSchema(BaseUserSchema):
    id: int
