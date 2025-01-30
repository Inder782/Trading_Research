import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt

plt.style.use('dark_background')
# Load the data
df = pd.read_csv("../data_csv/data_ETH_200_d.csv", parse_dates=["Date"], index_col=["Date"])

#logic to find

