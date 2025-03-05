import redis
import json

# Connect to Redis
r = redis.Redis(host="localhost", port=6379, db=0)

# Subscribe to the channel
p = r.pubsub()
p.subscribe("eth_data")

print("Waiting for data...")

# Listen for new messages
for message in p.listen():
    if message["type"] == "message":
        data = json.loads(message["data"])
        print("Received:", data['best_ask'])
