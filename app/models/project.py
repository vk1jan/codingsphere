from typing import Optional
from sqlmodel import Field
from datetime import datetime
from app.schemas.project import ProjectBase
from app.utils import get_utc_now

class Project(ProjectBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    created_at: datetime = Field(default_factory=get_utc_now)
    updated_at: datetime = Field(default_factory=get_utc_now)