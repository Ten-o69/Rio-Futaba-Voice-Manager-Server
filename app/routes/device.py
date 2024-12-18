from email.header import Header
from email.policy import default
from typing import Any, Annotated

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.crud.device import create_device, get_device_by_device_id
from app.schemas.device import DeviceCreate, DeviceResponse
from common.helpers import get_db
from common.constants import (
    API_SECRET_KEY,
)
from .utils import hash_password

router = APIRouter()


@router.post("/register", response_model=DeviceResponse)
def register_device(
    device: DeviceCreate,
    api_key: Annotated[str | None, Header(convert_underscores=False)] = None,
    db: Session = Depends(get_db)
) -> dict[str, Any]:
    """
        Регистрирует новое устройство.
    """
    print(api_key, API_SECRET_KEY)
    if api_key != API_SECRET_KEY:
        raise HTTPException(status_code=403, detail="Invalid API key")

    existing_device = get_device_by_device_id(db, device_id=device.device_id)

    if existing_device:
        raise HTTPException(status_code=400, detail="Device already registered")

    hashed_secret = hash_password(password=device.hashed_secret)
    new_device = create_device(
        db=db,
        device_id=device.device_id,
        hashed_secret=hashed_secret,
    )

    return new_device
