import pandas as pd
from sqlalchemy import create_engine, text
from nba_api.stats.endpoints import LeagueLeaders
import os

#pull data from api
leaders_24_25 = LeagueLeaders(season='2024-25').get_data_frames()[0]

#connect to postgresql using sqlaclhemy
DATABASE_URL = os.getenv('DATABASE_URL','postgresql://admin:admin@db:5432/nba_api')
engine = create_engine(DATABASE_URL)

leaders_24_25.to_sql('league_leaders',engine,if_exists="replace",index=False)