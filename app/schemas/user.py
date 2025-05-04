from typing import Optional
from enum import Enum
from sqlmodel import Field, SQLModel
from datetime import datetime
from pydantic import EmailStr

class Role(str, Enum):
    ADMIN = "admin"
    USER = "user"

class UserBase(SQLModel):
    username: str = Field(index=True, unique=True)
    email: Optional[EmailStr] = Field(default=None, index=True, unique=True)
    role: Role = Field(default=Role.USER)

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int
    created_at: datetime

class Token(SQLModel):
    access_token: str
    token_type: str

class TokenData(SQLModel):
    username: Optional[str] = None
    role: Optional[str] = None