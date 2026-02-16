from confluent_kafka import Consumer
import json

consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'nba-group',
    'auto.offset.reset': 'earliest'
})

consumer.subscribe(['nba-events'])

print("Listening for NBA events...")

while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print(f"Error: {msg.error()}")
        continue

    event = json.loads(msg.value())
    # Print the event - what would you print here?
    print(print(f"{event['player']} ({event['team']}) - {event['event']} | Q{event['quarter']} {event['game_clock']}")
)
