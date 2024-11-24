from datetime import datetime, timezone, timedelta
from uuid import uuid4
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from common.constants import (
    JWT_SECRET_KEY,
    JWT_ALGORITHM,
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES,
    JWT_REFRESH_TOKEN_EXPIRE_DAYS,
)
from app.models import (
    Token,
)

def create_access_token(data: dict) -> str:
    """
    Создаёт короткоживущий Access токен для устройства.
    """
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire, "type": "access"})

    return jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)

def create_refresh_token(db: Session, data: dict) -> str:
    """
    Создаёт Refresh токен для устройства и добавляем его в таблицу Token.
    """
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=JWT_REFRESH_TOKEN_EXPIRE_DAYS)  # 30 дней
    to_encode.update({"exp": expire, "type": "refresh"})
    jti = str(uuid4()) + str(expire) + str(uuid4())

    create_token = Token(
        jti=jti,
        device_id=data["id"],
        expires_at=expire,
    )

    db.add(create_token)
    db.commit()
    db.refresh(create_token)

    return jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)


def verify_token(token: str, expected_type: str) -> dict | None:
    """
    Проверяет JWT токен, возвращает данные, если токен валиден.
    """
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])

        # Проверяем тип токена
        if payload.get("type") != expected_type:
            raise JWTError("Invalid token type")

        # Проверяем срок действия
        if datetime.now(timezone.utc).timestamp() > payload.get("exp", 0):
            raise JWTError("Token has expired")

        return payload

    except JWTError:
        return None

def verify_access_token(token: str) -> dict | None:
    """
    Проверяет Access токен для устройства.
    """

    return verify_token(token, expected_type="access")

def verify_refresh_token(token: str, db: Session) -> dict | None:
    """
    Проверяет Refresh токен для устройства.
    """

    payload = verify_token(token, expected_type="refresh")

    if payload:
        db_token = db.query(Token).filter(Token.jti == payload["jti"]).first()

        if not db_token:
            raise JWTError("Token not found in database")

        if not db_token.is_active:
            raise JWTError("Token is not active")

        return db_token

    else:
        return None
