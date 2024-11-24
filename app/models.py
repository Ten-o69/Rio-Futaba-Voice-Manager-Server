from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


# Базовый класс для моделей SQLAlchemy
Base = declarative_base()


class Device(Base):
    """
    Модель физического устройства.
    """
    __tablename__ = 'devices'

    id = Column(Integer, primary_key=True, index=True)  # Уникальный идентификатор
    device_id = Column(String, unique=True, nullable=False, index=True)  # Уникальный ID устройства
    hashed_secret = Column(String, nullable=False)  # Хэшированный секретный ключ
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))  # Время регистрации
    updated_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc)
    )  # Время последнего обновления

    # Связь с токенами
    tokens = relationship("Token", back_populates="owner")


class Token(Base):
    """
    Модель для хранения Refresh токенов.
    """
    __tablename__ = 'tokens'

    id = Column(Integer, primary_key=True, index=True)  # Уникальный идентификатор
    jti = Column(String, unique=True, nullable=False)  # Сам JWT токен
    device_id = Column(Integer, ForeignKey('devices.id'), nullable=False)  # Внешний ключ на устройство
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))  # Время создания
    expires_at = Column(DateTime, nullable=False)  # Время истечения действия токена
    is_active = Column(Boolean, default=True)  # Статус токена (активный/отозванный)

    # Связь с устройством
    owner = relationship("Device", back_populates="tokens")


class File(Base):
    """
    Модель файла.
    """
    __tablename__ = 'files'

    id = Column(Integer, primary_key=True, index=True)  # Уникальный идентификатор
    client_id = Column(Integer, ForeignKey('devices.id'), nullable=False)  # Внешний ключ на клиента
    filename = Column(String, nullable=False)  # Имя файла
    file_path = Column(String, nullable=False)  # Путь к файлу
    uploaded_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))  # Время загрузки
    size = Column(BigInteger, nullable=False)  # Размер файла
    file_type = Column(String, nullable=False)  # Тип файла

    # Обратная связь с клиентом
    owner = relationship("Device", back_populates="files")
