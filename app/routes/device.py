from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.crud.device import create_client, get_client_by_email
from app.schemas.device import DeviceCreate, DeviceResponse
from common.helpers import get_db

router = APIRouter()


@router.post("/", response_model=DeviceResponse)
def create_client(
    client: DeviceCreate = Depends(create_client),
    db: Session = Depends(get_db)
):
    pass
