import json

from confluent_kafka import Consumer

from app.common.config import BOOTSTRAP_SERVERS, ORDER_TOPIC

consumer = Consumer({
    "bootstrap.servers": BOOTSTRAP_SERVERS,
    "group.id": "order-consumer-group",
    "auto.offset.reset": "earliest",
})

consumer.subscribe([ORDER_TOPIC])

print("Waiting for messages...")

try:
    while True:
        msg = consumer.poll(1.0)
        
        if msg is None:
            continue
        
        if msg.error():
            print(msg.error())
            continue
        
        event = json.loads(msg.value().decode("utf-8"))
        
        print("=" * 40)
        print("Received Event")
        print(json.dumps(event, indent=2))
        
except KeyboardInterrupt:
    print("Stopping consumer...")
    
finally:
    consumer.close()