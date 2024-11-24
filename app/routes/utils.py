import bcrypt


def hash_password(password: str) -> str:
    """
    Хэширует пароль с использованием bcrypt.

    :param password: Пароль в виде строки.
    :return: Хэшированный пароль в виде строки.
    """
    # Преобразуем пароль в байты
    password_bytes = password.encode('utf-8')

    # Генерируем соль
    salt = bcrypt.gensalt()

    # Хэшируем пароль
    hashed_password = bcrypt.hashpw(password_bytes, salt)

    # Возвращаем хэшированный пароль в виде строки
    return hashed_password.decode('utf-8')


def verify_password(password: str, hashed_password: str) -> bool:
    """
    Проверяет соответствие пароля и хэша.

    :param password: Обычный пароль в виде строки.
    :param hashed_password: Хэшированный пароль в виде строки.
    :return: True, если пароль совпадает с хэшем, иначе False.
    """
    # Преобразуем данные в байты
    password_bytes = password.encode('utf-8')
    hashed_password_bytes = hashed_password.encode('utf-8')

    # Сравниваем пароль с хэшем
    return bcrypt.checkpw(password_bytes, hashed_password_bytes)
