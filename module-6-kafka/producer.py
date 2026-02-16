from confluent_kafka import Producer
import json
import time
import random

producer = Producer({'bootstrap.servers': 'localhost:9092'})

players = ['Shai Gilgeous-Alexander', 'Luka Doncic', 'Nikola Jokic', 'Jayson Tatum', 'Anthony Edwards']
teams = ['OKC', 'DAL', 'DEN', 'BOS', 'MIN']
events = ['2PT Made', '3PT Made', 'Free Throw', 'Rebound', 'Assist', 'Turnover', 'Block', 'Steal']

for i in range(50):
    event = {
        'player': random.choice(players),
        'team': random.choice(teams),
        'event': random.choice(events),
        'quarter': random.randint(1, 4),
        'game_clock': f"{random.randint(0,11)}:{random.randint(0,59):02d}"
    }
    producer.produce('nba-events', json.dumps(event))
    print(f"Sent: {event}")
    time.sleep(1)

producer.flush()
print("Done sending events")
