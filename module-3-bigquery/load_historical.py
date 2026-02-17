import pandas as pd
from nba_api.stats.endpoints import LeagueLeaders
import time

headers = {
    'User-Agent': 'Mozilla/5.0',
    'Referer': 'https://www.nba.com/',
    'Accept': 'application/json'
}

seasons = ['2020-21', '2021-22', '2022-23', '2023-24', '2024-25']
all_data = []

for season in seasons:
    try:
        df = LeagueLeaders(season=season, headers=headers).get_data_frames()[0]
        df['SEASON'] = season
        all_data.append(df)
        print(f"Pulled {season}")
    except Exception as e:
        print(f"Failed {season}: {e}")
    time.sleep(5)

combined = pd.concat(all_data)

combined.to_gbq(
    destination_table='nba_stats.league_leaders_historical',
    project_id='nba-pipeline-1770915615',
    if_exists='replace'
)

print(f"Loaded {len(combined)} total rows to BigQuery")
