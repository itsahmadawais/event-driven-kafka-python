from abc import ABC
from datetime import datetime, timezone
from uuid import uuid4

from pydantic import BaseModel, Field

class Event(BaseModel):
   event_id: str = Field(default_factory=lambda: str(uuid4()))
   source: str
   occurred_at: datetime = Field(
       default_factory=lambda: datetime.now(timezone.utc)
    )
   
   @property
   def event_type(self) -> str:
       return NotImplementedError