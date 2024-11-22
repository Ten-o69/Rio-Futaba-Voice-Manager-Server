from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.crud.client import create_client, get_client_by_email
from app.schemas.client import ClientCreate, ClientBase, ClientResponse

router = APIRouter()


# @router.post("/")
