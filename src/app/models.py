# models.py

from pydantic import BaseModel
from typing import Optional
from uuid import UUID, uuid4


class IDCard(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    birth_date: str  # Format YYYY-MM-DD
    expiration_date: str  # Format YYYY-MM-DD
    is_active: bool = True
