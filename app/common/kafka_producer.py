import json

from confluent_kafka import Producer

class KafkaProducer:
    
    def __init__(self, bootstrap_servers: str):
        self.producer = Producer({
            "bootstrap.servers": bootstrap_servers,
        })
        
    def send(self, topic: str, event):
        self.producer.produce(
            topic=topic,
            value=json.dumps(event.model_dump(mode="json")).encode("utf-8"),
        )
        self.producer.flush()