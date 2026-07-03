import os

from dotenv import load_dotenv

load_dotenv()

BOOTSTRAP_SERVERS = os.getenv("BOOTSTRAP_SERVERS", "localhost:9092")
ORDER_TOPIC = os.getenv("ORDER_TOPIC", "orders")
PAYMENT_TOPIC = os.getenv("PAYMENT_TOPIC", "payments")