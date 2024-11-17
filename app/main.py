from fastapi import FastAPI
from app.routes import auth, commands, sync

app = FastAPI(title="Voice Manager API")

# Подключаем роуты
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(commands.router, prefix="/commands", tags=["Commands"])
app.include_router(sync.router, prefix="/sync", tags=["Synchronization"])

@app.get("/")
async def root():
    return {"message": "Voice Manager Server is running"}