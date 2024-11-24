from pydantic import BaseModel, EmailStr


class DeviceBase(BaseModel):
    device_id: str


class DeviceCreate(DeviceBase):
    hashed_secret: str


class DeviceResponse(DeviceBase):
    id: int
    device_id: int
    created_at: str

    class Config:
        orm_mode = True
