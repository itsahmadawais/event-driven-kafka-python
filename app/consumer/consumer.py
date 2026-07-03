import json
import sys

from confluent_kafka import Consumer

from app.common.config import BOOTSTRAP_SERVERS, ORDER_TOPIC

consumer_name = sys.argv[1] if len(sys.argv) > 1 else "Consumer"

def on_assign(consumer, partitions):
    print(f"\n🟢 {consumer_name} - Partitions Assigned")
    for partition in partitions:
        print(f"Topic: {partition.topic}, Partition: {partition.partition}")
        
    consumer.assign(partitions)
    
def on_revoke(consumer, partitions):
    print(f"\n🔴 {consumer_name} - Partitions Revoked")
    for partition in partitions:
        print(f"Topic: {partition.topic}, Partition: {partition.partition}")
    
consumer = Consumer({
    "bootstrap.servers": BOOTSTRAP_SERVERS,
    "group.id": "order-consumer-group",
    "auto.offset.reset": "earliest",
})

consumer.subscribe(
    [ORDER_TOPIC],
    on_assign=on_assign,
    on_revoke=on_revoke,
)

print(f"{consumer_name} waiting for messages...")

try:
    while True:
        msg = consumer.poll(1.0)
        
        if msg is None:
            continue
        
        if msg.error():
            print(msg.error())
            continue
        
        event = json.loads(msg.value().decode("utf-8"))
        
        print("=" * 50)
        print(f"{consumer_name}")
        print(f"Partition: {msg.partition()}")
        print(f"Offset: {msg.offset()}")
        print("Received Event")
        print(json.dumps(event, indent=2))
        
except KeyboardInterrupt:
    print("Stopping consumer...")
    
finally:
    consumer.close()