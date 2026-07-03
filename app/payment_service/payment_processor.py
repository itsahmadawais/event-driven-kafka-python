import json
import random
import time

from confluent_kafka import Consumer

from app.common.config import (
    BOOTSTRAP_SERVERS,
    ORDER_TOPIC,
    PAYMENT_TOPIC,
    DLQ_TOPIC
)
from app.common.kafka_producer import KafkaProducer
from app.events.payment_processed import (
    PaymentPayload,
    PaymentProcessedEvent,
)
from app.events.dead_letter_event import (
    DeadLetterEvent, 
    DeadLetterPayload
)

MAX_RETRIES = 3

consumer = Consumer({
    "bootstrap.servers": BOOTSTRAP_SERVERS,
    "group.id": "payment-service",
    "auto.offset.reset": "earliest",
    "enable.auto.commit": False,
})

consumer.subscribe([ORDER_TOPIC])

producer = KafkaProducer(BOOTSTRAP_SERVERS)

print("💳 Payment Service started...")

def publish_payment_processed(order):
    payment_event = PaymentProcessedEvent(
        source= "payment-service",
        payload=PaymentPayload(
            order_id=order["order_id"],
            payment_id=random.randint(1000, 9999),
            amount=order["amount"],
            status="SUCCESS"
        )
    )
    producer.send(
        topic=PAYMENT_TOPIC,
        event=payment_event,
        key=str(payment_event.payload.payment_id)
    )
    print("✅ PaymentProcessed published")
    
def publish_to_dlq(event, error:str, retry_count:int, msg):
    dlq_event = DeadLetterEvent(
        source="payment-service",
        payload = DeadLetterPayload(
            original_event=event,
            error=error,
            retry_count=retry_count,
            failed_service="payment-service",
            topic= msg.topic(),
            partition= msg.partition(),
            offset= msg.offset()
        ),
        topic=DLQ_TOPIC,
        partition=msg.partition(),
        offset=msg.offset()
    )
    producer.send(
        topic=DLQ_TOPIC,
        event=dlq_event,
        key=str(event["payload"]["order_id"])
    )
    print("📥 Sent to DLQ")
  
def process_payment(order):
    print("✅ Payment succeeded!")
    # Assuming Payment is successful, we publish the payment processed event
    return True
            
try:
    while True:
        msg = consumer.poll(1.0)
        
        if msg is None:
            continue
            
        if msg.error():
            print(msg.error())
            continue
        
        event = json.loads(msg.value().decode("utf-8"))
        order = event["payload"]
        
        print(f"💳 Processing payment for Order #{order['order_id']}")
        
        payment_successful = False
        
        for i in range(MAX_RETRIES):
            print(f"🔄 Attempt {i+1} of {MAX_RETRIES}...")
            if random.random() < 0.7:
                print("❌ Payment failed!")
                time.sleep(1)
            else:
                if process_payment(order):
                    publish_payment_processed(order)
                    payment_successful = True
                    consumer.commit(msg)
                    break
            
        if not payment_successful:
            error_msg = f"Payment failed after max({MAX_RETRIES}) retries"
            
            print(f"❌ {error_msg}")
            
            publish_to_dlq(
                event=event,
                error=error_msg,
                retry_count=MAX_RETRIES,
                msg=msg
            )
            
            consumer.commit(msg)
            
            
            
finally:
    consumer.close()