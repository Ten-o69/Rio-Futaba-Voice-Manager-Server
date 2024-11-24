from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base

from common.constants import DATABASE_URL


# Создаём движок SQLAlchemy
engine = create_engine(DATABASE_URL)

# Создаём сессии для взаимодействия с базой данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    """
    Создание всех таблиц в базе данных.
    """
    Base.metadata.create_all(bind=engine)


init_db()
