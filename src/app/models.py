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

    def convert_to_json_object(self):
        return {
            "id": str(self.id),
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date,
            "expiration_date": self.expiration_date,
            "is_active": str(self.is_active)
        }