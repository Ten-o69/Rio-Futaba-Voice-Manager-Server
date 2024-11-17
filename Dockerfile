# Используем базовый образ Python
FROM python:3.9-slim

# Указываем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей в контейнер
COPY requirements.txt requirements.txt

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код приложения в контейнер
COPY ./app ./app

# Указываем порт, который будет открыт
EXPOSE 8000

# Команда для запуска приложения
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]