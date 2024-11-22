from pydantic import BaseModel, EmailStr


class ClientBase(BaseModel):
    name: str
    email: EmailStr


class ClientCreate(ClientBase):
    password: str


class ClientResponse(ClientBase):
    id: int
    created_at: str

    class Config:
        orm_mode = True
