from typing import Literal
from pydantic import BaseModel, computed_field
from app.events.base_event import Event

class OrderPayload(BaseModel):
    order_id: int
    customer: str
    amount: float
    
class OrderCreatedEvent(Event):
    payload: OrderPayload
    
    @computed_field
    @property
    def event_type(self) -> Literal["OrderCreated"]:
        return "OrderCreated"