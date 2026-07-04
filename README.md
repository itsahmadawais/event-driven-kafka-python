# 🚀 Event-Driven Kafka with Python

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Apache Kafka](https://img.shields.io/badge/Apache-Kafka-orange)
![Docker](https://img.shields.io/badge/Docker-Compose-blue)
![License](https://img.shields.io/badge/License-MIT-green)

A hands-on project that explores **Apache Kafka** by building an **event-driven microservices architecture** in **Python**. Rather than focusing on isolated examples, this repository demonstrates how producers, consumers, topics, partitions, consumer groups, message keys, and event models work together in a realistic distributed system.

> **Status:** 🚧 In Progress — The project is being expanded incrementally as more advanced Kafka concepts are implemented.

---

## ✨ Features

* Event-driven architecture
* Apache Kafka producers and consumers
* Multiple microservices communicating through Kafka
* Strongly typed event models using Pydantic
* Docker-based local Kafka environment
* Kafka UI for inspecting topics and messages
* JSON event serialization
* Consumer Groups
* Topic Partitions
* Message Keys for ordering
* Consumer Rebalancing
* Modular Python project structure

---

## 🏗️ Current Architecture

```text
                    Kafka

        orders                  payments
           │                        │
           ▼                        ▼
   Payment Service         Notification Service
           ▲
           │
     Order Service
```

Event Flow

```text
Order Service
      │
      │ publishes OrderCreated
      ▼
   orders Topic
      │
      ▼
Payment Service
      │
      │ publishes PaymentProcessed
      ▼
 payments Topic
      │
      ▼
Notification Service
      │
      ▼
Customer Notification
```

---

## 🛠️ Tech Stack

* Python 3.14
* Apache Kafka
* Docker & Docker Compose
* Pydantic v2
* confluent-kafka

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

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/itsahmadawais/event-driven-kafka-python.git
cd event-driven-kafka-python
```

### 2. Create a virtual environment

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

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment

```bash
cp .env.example .env
```

Update the values if needed.

### 5. Start Kafka

```bash
cd docker
docker compose up -d
```

### 6. Start the Notification Service

```bash
python -m app.notification_service.notification_listener
```

### 7. Start the Payment Service

```bash
python -m app.payment_service.payment_processor
```

### 8. Publish an Order

```bash
python -m app.order_service.producer
```

---

## 📚 Kafka Concepts Covered

* Producers
* Consumers
* Topics
* Topic Partitions
* Offsets
* Consumer Groups
* Consumer Rebalancing
* Message Keys
* Event Ordering
* Event Serialization
* Event Modeling with Pydantic
* Event-Driven Architecture
* Service-to-Service Communication
* Kafka UI
* Docker-based Local Development

---

## 🗺️ Roadmap

* [x] Kafka Producer
* [x] Kafka Consumer
* [x] Event Models with Pydantic
* [x] Dockerized Kafka Environment
* [x] Multiple Partitions
* [x] Consumer Rebalancing
* [x] Message Keys
* [x] Event-Driven Microservices
* [x] Retry Strategy
* [x] Dead Letter Queue (DLQ)
* [x] Manual Offset Management
* [x] Idempotent Consumers
* [ ] Exactly-Once Processing
* [ ] Schema Registry & Avro
* [ ] Kafka Streams
* [ ] Integration Tests

---

## 🎯 Project Goal

The objective of this repository is not only to learn Kafka APIs but also to understand the architectural patterns used in production systems, including asynchronous communication, event-driven design, scalability, reliability, and fault tolerance.

---

## 📄 License

This project is licensed under the MIT License.
