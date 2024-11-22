import uuid
from app.database import SessionLocal


def get_db() -> SessionLocal:
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


def generate_uuid_name(name: str) -> str:
    """
    Генерирует uuid для любого имени
    :param name:
    :return:
    """
    return f"{name}-{uuid.uuid4().hex}"


def generate_uuid_filename(filename: str) -> str:
    """
    Генерирует uuid для имени файла
    :param filename:
    :return:
    """
    name_list = filename.split(".")
    filename = name_list[0]
    filetype = name_list[-1]

    return f"{filename}-{uuid.uuid4().hex}.{filetype}"
