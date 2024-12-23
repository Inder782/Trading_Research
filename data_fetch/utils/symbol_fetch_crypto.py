import ccxt
import pandas as pd

pd.set_option('display.max_columns', None)

exchange = ccxt.binance()
symbols=exchange.load_markets()

symbols_df=pd.DataFrame(symbols)
print(symbols_df.head())