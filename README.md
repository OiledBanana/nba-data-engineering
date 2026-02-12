# NBA Data Engineering Pipeline

An end-to-end data pipeline that ingests and analyzes NBA player stats.

## Architecture
(diagram coming soon)

## Tech Stack
- **Containerization:** Docker, Docker Compose
- **Database:** PostgreSQL
- **Orchestration:** Kestra
- **Infrastructure:** Terraform, GCP
- **Data Warehouse:** BigQuery
- **Transformations:** dbt
- **Batch Processing:** Apache Spark
- **Streaming:** Apache Kafka
- **Language:** Python, SQL

## Modules

### Module 1: Docker + Postgres
Dockerized Python script that pulls NBA league leaders from the nba_api and loads them into a PostgreSQL database.

### Module 2: Workflow Orchestration
Uses Kestra to automate the data pipeline on a daily schedule. The flow ingests the latest NBA stats into Postgres and queries the top scorers by points per game.

## Setup

```bash
git clone https://github.com/OiledBanana/nba-data-engineering.git
cd nba-data-engineering/module-1-docker-postgres
docker compose up -d
```
