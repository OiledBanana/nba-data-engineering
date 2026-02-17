import pandas as pd
from sqlalchemy import create_engine
from nba_api.stats.endpoints import LeagueLeaders
import os

# Pull data from NBA API
leaders_24_25 = LeagueLeaders(season='2024-25').get_data_frames()[0]

# Connect to PostgreSQL using SQLAlchemy
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://admin:admin@db:5432/nba_api')
engine = create_engine(DATABASE_URL)

# Load data into Postgres
leaders_24_25.to_sql('league_leaders', engine, if_exists='replace', index=False)
print(f"Loaded {len(leaders_24_25)} rows into league_leaders table")
