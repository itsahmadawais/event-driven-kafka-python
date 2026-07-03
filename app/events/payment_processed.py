from typing import Literal

from pydantic import BaseModel, computed_field

from app.events.base_event import Event


class PaymentPayload(BaseModel):
    order_id: int
    payment_id: int
    amount: float
    status: str
    
class PaymentProcessedEvent(Event):
    payload: PaymentPayload
    
    @computed_field
    @property
    def event_type(self) -> Literal["PaymentProcessed"]:
        return "PaymentProcessed"