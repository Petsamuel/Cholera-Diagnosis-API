# This project uses FastAPI 
# Author: samuel peter
# Source: https://github.com/Petsamuel/HandyMan-Backend
from pydantic import BaseModel, EmailStr, constr, validator, Field
from typing import Optional, List
from enum import Enum

class UserType(str, Enum):
    USER = "user"
    Admin = "admin"

class UserBase(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: EmailStr  
    phone: constr(min_length=10, max_length=15) = Field(..., pattern=r'^\+?\d{10,15}$')

class UserCreate(UserBase):
    user_type: Optional[UserType] = UserType.USER
    password: str

class User(UserBase):
    id: int

    class Config:
        form_attributes = True  # Use form_attributes for SQLAlchemy integration







class Token(BaseModel):
    access_token: str
    token_type: str
    user: Optional[User]  # Ensure User is defined before this line
    user_type: Optional[UserType]

    class Config:
        form_attributes = True

