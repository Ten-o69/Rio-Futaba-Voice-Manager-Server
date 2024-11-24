import os
from datetime import datetime
from datetime import UTC

from fastapi import (
    APIRouter,
    HTTPException,
    Depends,
    UploadFile,
    File
)
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.crud.device import get_device_by_device_id
from app.crud.file import upload_file as crud_upload_file
from app.schemas.file import FileCreate, FileBase, FileResponse
from app.auth import verify_access_token
from common.helpers import get_db, generate_uuid_filename
from common.constants import (
    PATH_UPLOAD_DIR,
)


router = APIRouter()


@router.post("/upload", response_model=FileResponse)
def upload_file(
        file: UploadFile = File(...),
        token: str = Depends(verify_access_token),
        db: Session = Depends(get_db),
):
    """
    Выгрузка файла. Авторизация обязательна.
    """
    # Проверяем токен
    if not token:
        raise HTTPException(
            status_code=401,
            detail="Invalid access token",
        )

    # Получаем клиента через CRUD
    client_email = token.get("sub")
    client = get_client_by_email(db, email=client_email)

    if not client:
        raise HTTPException(
            status_code=401,
            detail="Client not found.",
        )

    # Сохраняем файл на диск
    file.filename = generate_uuid_filename(file.filename)
    file_path = os.path.join(PATH_UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(file.file.read())


    file_record = crud_upload_file(
        db=db,
        client_id=client.client_id,
        filename=file.filename,
        file_path=file_path,
        uploaded_at=datetime.now(UTC),
        size=file.size,
        file_type=file.content_type,
    )

    json_response = {
        "message": "File uploaded successfully",
        "file_id": file_record.file_id,
    }

    return json_response


@router.get("/file/{file_id}", response_model=FileResponse)
def download_file(
    file_id: int,
    db: Session = Depends(get_db),
    token: str = Depends(verify_access_token),
):
    pass

