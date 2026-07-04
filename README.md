# 🚀 Event-Driven Kafka with Python

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Apache Kafka](https://img.shields.io/badge/Apache-Kafka-orange)
![Docker](https://img.shields.io/badge/Docker-Compose-blue)
![License](https://img.shields.io/badge/License-MIT-green)

A hands-on project for learning **Apache Kafka** by building an **event-driven microservices architecture** in **Python**. Rather than focusing on isolated examples, this repository demonstrates how producers, consumers, topics, partitions, consumer groups, message keys, retries, dead-letter queues, and idempotent consumers work together to build reliable distributed systems.

> **Status:** 🚧 In Progress — New Kafka concepts and production patterns will be added incrementally.

---

## ✨ Features

- Event-driven microservices architecture
- Apache Kafka producers and consumers
- Multiple services communicating asynchronously
- Strongly typed event models using Pydantic
- Docker-based local Kafka environment
- Kafka UI for inspecting topics and messages
- JSON event serialization
- Consumer Groups
- Topic Partitions
- Message Keys for event ordering
- Consumer Rebalancing
- Manual Offset Management
- Retry Strategy
- Dead Letter Queue (DLQ)
- Idempotent Consumer pattern
- Clean and modular Python project structure

---

# 🏗️ Architecture

```text
                  +----------------+
                  |  Order Service |
                  +-------+--------+
                          |
                    OrderCreated
                          |
                          ▼
                 +----------------+
                 |  orders Topic  |
                 +----------------+
                          |
                          ▼
                 +----------------+
                 | Payment Service|
                 +-------+--------+
                          |
                 PaymentProcessed
                          |
                          ▼
               +-------------------+
               |  payments Topic   |
               +-------------------+
                          |
                          ▼
              +----------------------+
              | Notification Service |
              +----------------------+
```

---

## 🔄 Event Flow

```text
Customer
    │
    ▼
Order Service
    │
    │ publishes OrderCreated
    ▼
orders Topic
    │
    ▼
Payment Service
    │
    ├── Retry on transient failures
    ├── Manual offset commit
    ├── Publish PaymentProcessed
    └── Publish DeadLetterEvent (after max retries)
    │
    ▼
payments Topic
    │
    ▼
Notification Service
    │
    ▼
Customer receives confirmation
```

---

## 🛡️ Reliability Features

The project demonstrates several techniques used in production event-driven systems.

- Manual Offset Management
- Retry Strategy
- Dead Letter Queue (DLQ)
- Idempotent Consumer Pattern
- Ordered event processing using Kafka message keys
- Consumer Groups and automatic rebalancing

---

## 📦 Event Models

All Kafka messages are represented using strongly typed **Pydantic** models.

Current events include:

- `OrderCreated`
- `PaymentProcessed`
- `DeadLetterEvent`

---

## 🛠️ Tech Stack

- Python 3.14
- Apache Kafka
- Docker & Docker Compose
- Pydantic v2
- confluent-kafka

---

## 📁 Project Structure

```text
.
├── app
│   ├── common
│   ├── events
│   ├── order_service
│   ├── payment_service
│   └── notification_service
│
├── docker
│   └── docker-compose.yml
│
├── .env.example
├── requirements.txt
├── README.md
└── LICENSE
```

---

# 🚀 Getting Started

## 1. Clone the repository

```bash
git clone https://github.com/itsahmadawais/event-driven-kafka-python.git
cd event-driven-kafka-python
```

## 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it.

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure environment

```bash
cp .env.example .env
```

Update the values if necessary.

---

## 5. Start Kafka

```bash
cd docker
docker compose up -d
```

---

## 6. Start the Notification Service

```bash
python -m app.notification_service.notification_listener
```

---

## 7. Start the Payment Service

```bash
python -m app.payment_service.payment_processor
```

---

## 8. Publish Orders

```bash
python -m app.order_service.producer
```

---

## 📚 Kafka Concepts Covered

This repository currently demonstrates:

- Producers
- Consumers
- Topics
- Topic Partitions
- Offsets
- Consumer Groups
- Consumer Rebalancing
- Message Keys
- Event Ordering
- Event Serialization
- Event Modeling with Pydantic
- Event-Driven Architecture
- Service-to-Service Communication
- Retry Strategy
- Manual Offset Management
- Dead Letter Queues (DLQ)
- Idempotent Consumers
- Kafka UI
- Docker-based Local Development

---

## 🗺️ Roadmap

### ✅ Completed

- [x] Kafka Producers
- [x] Kafka Consumers
- [x] Event Models with Pydantic
- [x] Dockerized Kafka Environment
- [x] Multiple Partitions
- [x] Consumer Groups
- [x] Consumer Rebalancing
- [x] Message Keys
- [x] Event Ordering
- [x] Event-Driven Microservices
- [x] Retry Strategy
- [x] Manual Offset Management
- [x] Dead Letter Queue (DLQ)
- [x] Idempotent Consumers

### 🚧 Planned

- [ ] Kafka Transactions (Exactly-Once Semantics)
- [ ] Schema Registry & Avro
- [ ] Transactional Outbox Pattern
- [ ] Persistent Idempotency Store (PostgreSQL/Redis)
- [ ] Integration Tests

---

## 🎯 Project Goal

The goal of this repository is to understand not only Kafka APIs but also the architectural patterns used in modern distributed systems.

Topics include:

- Event-Driven Architecture
- Asynchronous Communication
- Reliable Event Processing
- Fault Tolerance
- Ordering Guarantees
- Retry Mechanisms
- Dead Letter Queues
- Consumer Scalability
- Microservice Communication Patterns

This repository serves as a practical learning resource for backend engineers who want to understand how Kafka is used in real-world systems.

---

## 📄 License

This project is licensed under the MIT License.