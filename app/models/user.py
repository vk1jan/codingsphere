from typing import Optional
from sqlmodel import Field
from datetime import datetime
from app.schemas.user import UserBase
from app.utils import get_utc_now

class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    hashed_password: str
    created_at: datetime = Field(default_factory=get_utc_now)
    updated_at: datetime = Field(default_factory=get_utc_now)
