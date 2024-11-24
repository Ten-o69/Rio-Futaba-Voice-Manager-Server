from fastapi import FastAPI
from app.routes import device, file

app = FastAPI(title="Voice Manager API")

# Подключаем роуты
app.include_router(device.router, prefix="/devices", tags=["Devices"])

@app.get("/")
async def root():
    return {"message": "Voice Manager Server is running"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
