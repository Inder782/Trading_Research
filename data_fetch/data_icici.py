from breeze_connect import BreezeConnect
from dotenv import load_dotenv
import os
import pandas as pd
from utils.date_time_util import convert_date

load_dotenv()


"""
file contains the functions to get equity , futures and options 
historical data from ICICI breeze api.
"""
# env files
api = os.environ["API_KEY"]
secret = os.environ["SECRET_KEY"]
session = os.environ["SESSION_KEY"]

# generate session
breeze = BreezeConnect(api_key=api)

breeze.generate_session(api_secret=secret, session_token=session)


def equity_historical(symbol: str, start: str, end: str, timeframe: str):
    raw_data = breeze.get_historical_data_v2(
        interval=timeframe,
        from_date=convert_date(start),
        to_date=convert_date(end),
        stock_code=symbol,
        exchange_code="NSE",
        product_type="cash",
    )

    raw_frame = pd.DataFrame(raw_data["Success"])

    final_frame = raw_frame[["datetime", "open", "high", "low", "close", "volume"]]
    # change the column date to stock name
    final_frame.rename(columns={"datetime": symbol})

    return final_frame


def fut_historical(symbol: str, start: str, end: str, timeframe: str, expiry: str):
    raw_data = breeze.get_historical_data_v2(
        interval=timeframe,
        from_date=convert_date(start),
        to_date=convert_date(end),
        stock_code=symbol,
        exchange_code="NFO",
        product_type="futures",
        expiry_date=convert_date(expiry),
        right="others",
        strike_price="0",
    )
    raw_frame = pd.DataFrame(raw_data["Success"])

    final_frame = raw_frame[["datetime", "open", "high", "low", "close", "volume"]]
    # change the column date to stock name
    final_frame.rename(columns={"datetime": symbol}, inplace=True)

    return final_frame


symbol = "NIFTY"
date_start = "01-10-2006"
date_end = "25-12-2024"
timeframe = "1day"  # can be 1minute , 5minute , 30minute, 1 day
expiry = "26-12-2024"  # if fut

data = equity_historical(symbol, date_start, date_end, timeframe)

# rename the file and save it
data.to_csv(f"{symbol}_{date_start}_to_{date_end}_{timeframe}.csv", index=False)
