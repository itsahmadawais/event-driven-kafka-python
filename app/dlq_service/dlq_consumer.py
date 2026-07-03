import json

from confluent_kafka import Consumer

from app.common.config import BOOTSTRAP_SERVERS

from app.common.config import DLQ_TOPIC


consumer = Consumer({
    "bootstrap.servers": BOOTSTRAP_SERVERS,
    "group.id": "dlq-consumer",
    "auto.offset.reset": "earliest",
})

consumer.subscribe([DLQ_TOPIC])

print("🚨 DLQ Consumer started...")


try:
    while True:
        msg = consumer.poll(1.0)
        
        if msg is None:
            continue
        
        if msg.error():
            print(msg.error())
            continue
        
        event = json.loads(msg.value().decode("utf-8"))
        
        
        print("\n" + "=" * 60)
        print("🚨 DEAD LETTER EVENT RECEIVED")
        print("=" * 60)
        
        print(json.dumps(event, indent=2))
        
        payload = event["payload"]
        print("\n📌 Summary:")
        print(f"Service: {payload['failed_service']}")
        print(f"Error: {payload['error']}")
        print(f"Retries: {payload['retry_count']}")
        print(f"Original Event Type: {payload['original_event']['event_type']}")

except KeyboardInterrupt:
    print("\n🛑 Stopping DLQ Consumer...")
        
finally:
    consumer.close()