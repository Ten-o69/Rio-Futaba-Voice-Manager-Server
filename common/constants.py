import os
from pathlib import Path
from dotenv import load_dotenv

# paths
PROJECT_ROOT = Path(__file__).parent.parent
PATH_CONFIG_MODULE = os.path.join(PROJECT_ROOT, "config")
PATH_SECRETS_FILE = os.path.join(PATH_CONFIG_MODULE, "secrets.env")
PATH_UPLOAD_DIR = os.path.join(PROJECT_ROOT, "files")

load_dotenv(PATH_SECRETS_FILE)

# db
DATABASE_URL = os.getenv("DATABASE_URL")

# jwt
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")  # Секретный ключ
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")  # Алгоритм подписи токенов
JWT_ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRE_MINUTES"))  # Время жизни access-токена (в минутах)
JWT_REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("JWT_REFRESH_TOKEN_EXPIRE_DAYS"))  # Время жизни refresh-токена (в днях)

# api secret key
API_SECRET_KEY = os.getenv("API_SECRET_KEY")
