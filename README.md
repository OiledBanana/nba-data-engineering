# NBA Data Engineering Pipeline

An end-to-end data engineering pipeline that ingests, transforms, and analyzes NBA player statistics across 15 seasons using modern data stack tools.

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Containerization | Docker, Docker Compose |
| Database | PostgreSQL |
| Orchestration | Kestra |
| Cloud Platform | Google Cloud Platform |
| Data Warehouse | BigQuery |
| Transformations | dbt |
| Batch Processing | Apache Spark |
| Streaming | Apache Kafka |
| Language | Python, SQL |

## Project Structure

```
nba-data-engineering/
├── module-1-docker-postgres/   # Containerized ingestion pipeline
│   ├── docker-compose.yml
│   ├── Dockerfile
│   ├── ingest.py
│   └── requirements.txt
├── module-2/                   # Workflow orchestration
│   ├── docker-compose.yml
│   └── flows/
│       └── nba_ingest.yml
├── module-3-bigquery/          # Cloud data warehouse
│   ├── load_to_bigquery.py
│   └── load_historical.py
├── module-4-dbt/               # Analytics engineering
│   └── nba_transform/
│       └── models/
│           ├── staging/
│           │   └── stg_league_leaders.sql
│           └── marts/
│               └── mvp_candidates.sql
├── module-5-spark/             # Batch processing
│   ├── export_data.py
│   └── spark_analysis.py
└── module-6-kafka/             # Real-time streaming
    ├── docker-compose.yml
    ├── producer.py
    └── consumer.py
```

## Modules

### Module 1: Docker + PostgreSQL
Containerized Python pipeline that pulls current NBA league leaders from the NBA API and loads them into a PostgreSQL database using Docker Compose.

**Key concepts:** Docker multi-service networking, volume persistence, environment variables, Python data ingestion

### Module 2: Workflow Orchestration (Kestra)
Automated daily pipeline using Kestra that ingests the latest NBA stats and runs analytical queries on a schedule.

**Key concepts:** DAG-based orchestration, scheduled triggers, task chaining, containerized workflows

### Module 3: BigQuery Data Warehouse
Loads 5 seasons of NBA league leaders into Google BigQuery for cross-season analytical queries at scale.

**Key concepts:** Cloud data warehousing, API rate limiting, batch loading, GCP authentication

### Module 4: Analytics Engineering (dbt)
Transforms raw NBA data into clean staging and mart models with automated data quality tests.

- **Staging:** Renames columns, computes per-game averages (PPG, RPG, APG)
- **Mart:** MVP candidates filtered by games played, ranked by scoring

**Key concepts:** dbt source/ref, staging vs mart layers, schema tests, incremental models

### Module 5: Batch Processing (Apache Spark)
Processes 15 seasons of historical NBA data (7,758 rows) using Spark SQL to find all-time scoring leaders and team representation trends.

**Key concepts:** SparkSession, Spark SQL, temporary views, distributed processing

### Module 6: Real-Time Streaming (Apache Kafka)
Simulates live NBA game events with a Kafka producer/consumer pattern. The producer generates play-by-play events and the consumer processes them in real time.

**Key concepts:** Kafka topics, producer/consumer pattern, Zookeeper coordination, event-driven architecture

## Getting Started

### Prerequisites
- Docker & Docker Compose
- Python 3.10+
- Google Cloud SDK (for Module 3+)
- Apache Spark (for Module 5)

### Quick Start

```bash
git clone https://github.com/OiledBanana/nba-data-engineering.git
cd nba-data-engineering

# Module 1: Run the ingestion pipeline
cd module-1-docker-postgres
docker compose up -d

# Verify data loaded
docker exec -it nba_api psql -U admin -d nba_api -c "SELECT COUNT(*) FROM league_leaders;"
```

### GCP Setup (Modules 3-4)

1. Create a Google Cloud account at [cloud.google.com/free](https://cloud.google.com/free)
2. Install Google Cloud SDK
3. Initialize and create a project:
```bash
gcloud init
gcloud projects create YOUR-PROJECT-ID
gcloud config set project YOUR-PROJECT-ID
```
4. Link a billing account (free trial includes $300 in credits)
5. Enable required APIs:
```bash
gcloud services enable bigquery.googleapis.com storage.googleapis.com
```
6. Authenticate:
```bash
gcloud auth application-default login
```

## Data Source

All data is sourced from the [nba_api](https://github.com/swar/nba_api) Python package, which provides access to NBA.com stats endpoints including league leaders, player stats, and game logs.
