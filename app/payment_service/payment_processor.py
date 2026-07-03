import json
import random

from confluent_kafka import Consumer

from app.common.config import (
    BOOTSTRAP_SERVERS,
    ORDER_TOPIC,
    PAYMENT_TOPIC
)
from app.common.kafka_producer import KafkaProducer
from app.events.payment_processed import (
    PaymentPayload,
    PaymentProcessedEvent
)


consumer = Consumer({
    "bootstrap.servers": BOOTSTRAP_SERVERS,
    "group.id": "payment-service",
    "auto.offset.reset": "earliest",
})

consumer.subscribe([ORDER_TOPIC])

producer = KafkaProducer(BOOTSTRAP_SERVERS)

print("💳 Payment Service started...")

try:
    while True:
        msg = consumer.poll(1.0)
        
        if msg is None:
            continue
            
        if msg.error():
            print(msg.error())
            continue
        
        event = json.loads(msg.value().decode("utf-8"))
        
        print(f"💳 Processing payment for Order #{event['payload']['order_id']}")
        
        payment_event = PaymentProcessedEvent(
            source= "payment-service",
            payload=PaymentPayload(
                order_id=event["payload"]["order_id"],
                payment_id=random.randint(1000, 9999),
                amount=event["payload"]["amount"],
                status="SUCCESS"
            )
        )
        producer.send(
            topic=PAYMENT_TOPIC,
            event=payment_event,
            key=str(payment_event.payload.payment_id)
        )
        print("✅ PaymentProcessed published")
        
finally:
    consumer.close()