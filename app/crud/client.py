import email

from sqlalchemy.orm import Session
from app.models import Client
from app.auth import create_access_token, create_refresh_token


def create_client(db: Session, name: str, email: str, hashed_password: str) -> dict:
    """
    Создаёт нового клиента в базе данных и возвращает токены.
    """
    new_client = Client(name=name, email=email, hashed_password=hashed_password)
    db.add(new_client)
    db.commit()
    db.refresh(new_client)

    # Генерация токенов
    access_token = create_access_token(
        {
            "client_id": new_client.id,
            "email": new_client.email,
        }
    )
    refresh_token = create_refresh_token(
        {
            "client_id": new_client.id,
            "email": new_client.email,
        }
    )

    response_json = {
        "client": new_client,
        "access_token": access_token,
        "refresh_token": refresh_token,
    }

    return response_json


def get_client_by_email(db: Session, email: str):
    """
    Получает клиента по email.
    """

    return db.query(Client).filter(Client.email == email).first()
