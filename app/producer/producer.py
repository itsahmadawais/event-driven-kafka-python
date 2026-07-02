from app.common.config import BOOTSTRAP_SERVERS, ORDER_TOPIC
from app.common.kafka_producer import KafkaProducer
from app.events.order_created import OrderCreatedEvent, OrderPayload

producer = KafkaProducer(BOOTSTRAP_SERVERS)

event = OrderCreatedEvent(
    source="order-service",
    payload=OrderPayload(
        order_id=1,
        customer="Awais",
        amount=500.00,
    )
)

producer.send(ORDER_TOPIC, event)


print("✅ Event sent successfully")