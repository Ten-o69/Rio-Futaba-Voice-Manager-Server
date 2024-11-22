from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.auth import verify_access_token, verify_refresh_token


# Схема OAuth2 для передачи токена через заголовок Authorization
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_current_client(token: str = Depends(oauth2_scheme)):
    """
    Проверяет access token и возвращает данные клиента.
    """
    payload = verify_access_token(token)

    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired access token")

    return payload


def get_refresh_client(token: str = Depends(oauth2_scheme)):
    """
    Проверяет refresh token и возвращает данные клиента.
    """
    payload = verify_refresh_token(token)

    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired refresh token")

    return payload
