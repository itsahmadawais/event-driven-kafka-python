from app.events.base_event import Event
from pydantic import BaseModel

class DeadLetterPayload(BaseModel):
    original_event: dict
    error: str
    retry_count: int
    failed_service: str
    topic: str
    partition: int
    offset: int
    
class DeadLetterEvent(Event):
    payload: DeadLetterPayload