import ccxt
import pandas as pd
import datetime

# Initialize Binance exchange
exchange = ccxt.binance()


def crypto_historical(symbol: str, timeframe: str, start) -> pd.DataFrame:
    # date_modify
    start = datetime.datetime.strptime(start, "%Y-%m-%d").isoformat() + "Z"

    raw_data = exchange.fetch_ohlcv(symbol, timeframe, since=exchange.parse8601(start))

    # create a pandas dataframe
    data = pd.DataFrame(raw_data)

    # rename columns
    data = data.rename(
        columns={0: "Date", 1: "Open", 2: "High", 3: "Low", 4: "Close", 5: "Volume"}
    )

    # convert date
    data["Date"] = data["Date"].apply(
        lambda x: datetime.datetime.fromtimestamp(x / 1000)
    )

    return data


# Fetch historical data
symbol = "BTC/USDT"
timeframe = "1d"  # Supported: '1m', '5m', '1h', '1d', etc.
since = "2024-12-12"  # Start date

data = crypto_historical(symbol, timeframe, since)
print(data)
