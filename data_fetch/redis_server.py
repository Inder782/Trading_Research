import asyncio
import ccxt.pro as ccxt
import redis
import json

# Connect to Redis
r = redis.Redis(host="localhost", port=6379, db=0)

async def fetch_order_book():
    exchange = ccxt.binance()  # Initialize Exchange
    
    try:
        await exchange.load_markets()
        symbol = "ETH/USDT"

        while True:
             order_book = await exchange.watch_order_book(symbol)
             message = {
                "symbol": symbol,
                "best_ask": order_book['asks'][0],
                "best_bid": order_book['bids'][0],
                "timestamp": order_book['timestamp']
            }
             r.publish("eth_data", json.dumps(message))
             print("Published:", message)
        
    except Exception as e:
        print("Error:", e)

    finally:
        await exchange.close()  # Ensure WebSocket is closed properly

# Run event loop
asyncio.run(fetch_order_book())
