from pydantic import BaseModel


class FileBase(BaseModel):
    filename: str
    file_type: str
    file_size: int


class FileCreate(FileBase):
    client_id: int
    file_path: str


class FileResponse(FileBase):
    id: int
    uploaded_at: str

    class Config:
        orm_mode = True
