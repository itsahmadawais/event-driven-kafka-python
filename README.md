# 🚀 Event-Driven Kafka with Python

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Apache Kafka](https://img.shields.io/badge/Apache-Kafka-orange)
![Docker](https://img.shields.io/badge/Docker-Compose-blue)
![License](https://img.shields.io/badge/License-MIT-green)

A hands-on project that explores **Apache Kafka** by building an event-driven system in **Python**. Rather than focusing on isolated code snippets, this repository demonstrates how producers, consumers, topics, partitions, consumer groups, and event models work together in a real-world architecture.

> **Status:** 🚧 In Progress — New concepts and services will be added as the project evolves.

---

## ✨ Features

* Event-driven architecture
* Apache Kafka producer implementation
* Apache Kafka consumer implementation
* Strongly typed event models using Pydantic
* Docker-based local Kafka environment
* Kafka UI for topic inspection
* JSON event serialization
* Modular Python project structure

---

## 🛠️ Tech Stack

* Python 3.14
* Apache Kafka
* Docker & Docker Compose
* Pydantic
* confluent-kafka

---

## 📁 Project Structure

```text
.
├── app
│   ├── common
│   ├── consumer
│   ├── events
│   ├── producer
│   └── services
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
git clone <repository-url>
cd event-driven-kafka-python
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it.

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

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
docker compose up -d
```

### 6. Run the Consumer

```bash
python -m app.consumer.consumer
```

### 7. Publish an Event

```bash
python -m app.producer.producer
```

---

## 📚 Kafka Concepts Covered

* Producers
* Consumers
* Topics
* Offsets
* Consumer Groups
* Event Serialization
* Event Modeling
* Kafka UI
* Docker-based Local Development

---

## 🗺️ Roadmap

* [x] Kafka Producer
* [x] Kafka Consumer
* [x] Event Models with Pydantic
* [x] Dockerized Kafka Environment
* [ ] Multiple Partitions
* [ ] Consumer Rebalancing
* [ ] Message Keys
* [ ] Retry Strategy
* [ ] Dead Letter Queue (DLQ)
* [ ] Manual Offset Management
* [ ] Multiple Microservices
* [ ] Idempotent Consumers
* [ ] Exactly-Once Processing
* [ ] Integration Tests

---

## 📄 License

This project is licensed under the MIT License.
