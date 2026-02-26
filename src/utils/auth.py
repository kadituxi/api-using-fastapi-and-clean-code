import datetime
import os

from dotenv import load_dotenv
from jose import jwt, exceptions

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt


def decode_token(token: str) -> dict:
    try:
        token_data = jwt.decode(token, SECRET_KEY)
        return token_data
    except exceptions.JWTError as e:
        print(str(e))
        return {}
