from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Базовый класс для моделей SQLAlchemy
Base = declarative_base()

class Client(Base):
    """
    Модель клиента.
    """
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True, index=True)  # Уникальный идентификатор
    name = Column(String, nullable=False)  # Имя клиента
    email = Column(String, unique=True, nullable=False, index=True)  # Уникальная почта
    hashed_password = Column(String, nullable=False)  # Хэшированный пароль
    created_at = Column(DateTime, default=datetime.utcnow)  # Время создания
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)  # Время обновления

    # Связь с токенами (один ко многим)
    tokens = relationship("Token", back_populates="owner")

    # Связь с файлами (один ко многим)
    files = relationship("File", back_populates="owner")

class Token(Base):
    """
    Модель токена.
    """
    __tablename__ = 'tokens'

    id = Column(Integer, primary_key=True, index=True)  # Уникальный идентификатор
    token = Column(String, unique=True, nullable=False)  # Сам JWT-токен
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)  # Внешний ключ на клиента
    created_at = Column(DateTime, default=datetime.utcnow)  # Время создания
    expires_at = Column(DateTime, nullable=False)  # Время истечения действия токена
    is_active = Column(Boolean, default=True)  # Статус токена (активный/отозванный)

    # Обратная связь с клиентом
    owner = relationship("Client", back_populates="tokens")

class File(Base):
    """
    Модель файла.
    """
    __tablename__ = 'files'

    id = Column(Integer, primary_key=True, index=True)  # Уникальный идентификатор
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)  # Внешний ключ на клиента
    filename = Column(String, nullable=False)  # Имя файла
    file_path = Column(String, nullable=False)  # Путь к файлу
    uploaded_at = Column(DateTime, default=datetime.utcnow)  # Время загрузки
    size = Column(BigInteger, nullable=False)  # Размер файла
    file_type = Column(String, nullable=False)  # Тип файла

    # Обратная связь с клиентом
    owner = relationship("Client", back_populates="files")
