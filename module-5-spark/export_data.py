import pandas as pd
from nba_api.stats.endpoints import LeagueLeaders
import time

seasons = [f"{y}-{str(y+1)[-2:]}" for y in range(2010, 2025)]
all_data = []

for season in seasons:
    try:
        df = LeagueLeaders(season=season, headers={'User-Agent': 'Mozilla/5.0', 'Referer': 'https://www.nba.com/', 'Accept': 'application/json'}).get_data_frames()[0]
        df['SEASON'] = season
        all_data.append(df)
        print(f"Pulled {season}")
    except Exception as e:
        print(f"Failed {season}: {e}")
    time.sleep(5)

combined = pd.concat(all_data)
combined.to_csv('nba_historical.csv', index=False)
print(f"Saved {len(combined)} rows")
