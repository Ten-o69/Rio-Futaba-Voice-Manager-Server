from sqlalchemy.orm import Session
from app.models import File


def upload_file(
        db: Session,
        client_id: int,
        filename: str,
        file_path: str,
        size: int,
        file_type: str
):
    """
    Загружает файл в базу данных.
    """
    new_file = File(
        client_id=client_id,
        filename=filename,
        file_path=file_path,
        size=size,
        file_type=file_type,
    )
    db.add(new_file)
    db.commit()
    db.refresh(new_file)

    return new_file


def get_files_by_client_id(db: Session, client_id: int):
    """
    Получает список файлов клиента.
    """
    return db.query(File).filter(File.client_id == client_id).all()


def delete_file(db: Session, file_id: int):
    """
    Удаляет файл из бд
    :param db:
    :param file_id:
    :return:
    """
    file = db.query(File).filter(File.client_id == file_id).first()

    if file:
        db.delete(file)
        db.commit()
