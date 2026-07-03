from app.common.config import BOOTSTRAP_SERVERS, ORDER_TOPIC
from app.common.kafka_producer import KafkaProducer
from app.events.order_created import OrderCreatedEvent, OrderPayload

producer = KafkaProducer(BOOTSTRAP_SERVERS)

order_id = 1

try:
    while True:
        customer = input("Customer Name:")
        amount = float(input("Amount:"))
        
        event = OrderCreatedEvent(
            source="order-service",
            payload=OrderPayload(
                order_id=order_id,
                customer=customer,
                amount=amount,
            )
        )

        producer.send(
            topic=ORDER_TOPIC, 
            key=str(event.payload.order_id),
            event=event
        )
        
        order_id += 1
        print("✅ Event sent successfully")

except KeyboardInterrupt:
    print("\n🔴 Order Service stopped")