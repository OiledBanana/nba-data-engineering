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

### Module 3: BigQuery Data Warehouse
Loads NBA league leaders into BigQuery including 5 seasons of historical data for cross-season analysis.

## GCP Setup

1. Create a Google Cloud account at cloud.google.com/free
2. Install Google Cloud SDK
3. Log in and create a project:
```bash
gcloud init
gcloud projects create YOUR-PROJECT-ID
gcloud config set project YOUR-PROJECT-ID


```bash
git clone https://github.com/OiledBanana/nba-data-engineering.git
cd nba-data-engineering/module-1-docker-postgres
docker compose up -d
```
