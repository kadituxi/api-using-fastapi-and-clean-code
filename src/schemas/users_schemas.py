from pydantic import BaseModel, EmailStr, Field


class BaseUserSchema(BaseModel):
    name: str = Field(min_length=5)
    email: EmailStr = Field(min_length=5)


class LoginUserSchema(BaseModel):
    email: EmailStr = Field(min_length=5)
    password: str = Field(min_length=8)


class RegisterUserSchema(BaseUserSchema):
    password: str = Field(min_length=8)


class ResponseUserSchema(BaseUserSchema):
    id: int


class TokenSchema(BaseModel):
    access_token: str
    token_type: str = "bearer"
