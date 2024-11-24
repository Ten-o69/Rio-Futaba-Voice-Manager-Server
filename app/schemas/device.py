from datetime import datetime
from pydantic import BaseModel


class DeviceBase(BaseModel):
    device_id: str


class DeviceCreate(DeviceBase):
    hashed_secret: str


class DeviceResponse(DeviceBase):
    id: int
    created_at: datetime
    access_token: str
    refresh_token: str

    class Config:
        orm_mode = True
