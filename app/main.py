from fastapi import FastAPI
from app.routes import device, file

app = FastAPI(title="Voice Manager API")

# Подключаем роуты


@app.get("/")
async def root():
    return {"message": "Voice Manager Server is running"}