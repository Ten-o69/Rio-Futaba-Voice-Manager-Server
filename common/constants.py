import os
from dotenv import load_dotenv

# paths
CDIR = os.getcwd() + "/"
PATH_CONFIG_MODULE = os.path.join(CDIR, "config")
PATH_SECRETS_FILE = os.path.join(CDIR, "secrets.env")
PATH_UPLOAD_DIR = os.path.join(CDIR, "../files")

load_dotenv(PATH_SECRETS_FILE)

# db
DATABASE_URL = os.getenv("DATABASE_URL")

# jwt
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")  # Секретный ключ
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")  # Алгоритм подписи токенов
JWT_ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("JWT_ACCESS_TOKEN_EXPIRE_MINUTES")  # Время жизни access-токена (в минутах)
JWT_REFRESH_TOKEN_EXPIRE_DAYS = os.getenv("JWT_REFRESH_TOKEN_EXPIRE_DAYS")  # Время жизни refresh-токена (в днях)
