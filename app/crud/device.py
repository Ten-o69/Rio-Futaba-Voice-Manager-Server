from sqlalchemy.orm import Session
from app.models import Device
from app.auth import create_access_token, create_refresh_token


def create_device(
        db: Session,
        device_id: str,
        hashed_secret: str,
) -> dict:
    """
    Создаёт нового клиента в базе данных и возвращает токены.
    """
    new_device = Device(
        device_id=device_id,
        hashed_secret=hashed_secret,
    )

    db.add(new_device)
    db.commit()
    db.refresh(new_device)

    # Генерация токенов
    access_token = create_access_token(
        {
            "id": new_device.id,
            "device_id": new_device.device_id,
        }
    )

    refresh_token = create_refresh_token(
        db,
        {
            "id": new_device.id,
            "device_id": new_device.device_id,
        },
    )

    response_json = {
        "id": new_device.id,
        "device_id": new_device.device_id,
        "created_at": new_device.created_at,
        "access_token": access_token,
        "refresh_token": refresh_token,
    }

    return response_json


def get_device_by_device_id(db: Session, device_id: str):
    """
    Получает клиента по device_id.
    """

    return db.query(Device).filter(Device.device_id == device_id).first()
