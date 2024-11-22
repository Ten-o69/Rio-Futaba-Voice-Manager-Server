from datetime import datetime, timedelta
from jose import jwt, JWTError
from pydantic import ValidationError

from common.constants import (
    JWT_SECRET_KEY,
    JWT_ALGORITHM,
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES,
    JWT_REFRESH_TOKEN_EXPIRE_DAYS,
)

def create_access_token(data: dict):
    """
    Создаёт короткоживущий токен доступа (access token).
    :param data:
    :return:
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(milliseconds=JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire, "type": "access"})

    return jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)


def create_refresh_token(data: dict):
    """
    Создаёт длинно живущий токен обновления (refresh token).
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(milliseconds=JWT_REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire, "type": "refresh"})

    return jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)


def verify_access_token(token: str):
    """
    Проверяет короткоживущий токен доступа (access token).
    """
    return verify_token(token, expected_type="access")


def verify_refresh_token(token: str):
    """
    Проверяет длинноживущий токен обновления (refresh token).
    """
    return verify_token(token, expected_type="refresh")
