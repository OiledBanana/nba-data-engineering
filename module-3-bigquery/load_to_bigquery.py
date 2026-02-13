import pandas as pd
from nba_api.stats.endpoints import LeagueLeaders

leaders = LeagueLeaders(season='2024-25').get_data_frames()[0]

leaders.to_gbq(
    destination_table='nba_stats.league_leaders',
    project_id='nba-pipeline-1770915615',
    if_exists='replace'
)

print(f"Loaded {len(leaders)} rows to BigQuery")