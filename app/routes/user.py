# This project uses FastAPI 
# Author: samuel peter
# Source: https://github.com/Petsamuel/cholera-diagnosis-Backend
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import model
from app.schemas import schema
from app.database import get_db
from passlib.context import CryptContext
import bcrypt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=schema.User)
async def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    db_user = model.User(username=user.username, email=user.email, first_name=user.first_name, last_name=user.last_name, phone=user.phone, hashed_password = pwd_context.hash(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/{user_id}", response_model=schema.User)
async def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(model.User).filter(model.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
