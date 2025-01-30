import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt

plt.style.use('dark_background')
# Load the data
df = pd.read_csv("../data_csv/data_ETH_200_d.csv", parse_dates=["Date"], index_col=["Date"])

def support(df1, l, n1, n2): #n1 n2 before and after candle l
    for i in range(l-n1+1, l+1):
        if(df1.Low[i]>df1.Low[i-1]):
            return 0
    for i in range(l+1,l+n2+1):
        if(df1.Low[i]<df1.Low[i-1]):
            return 0
    return 1

some=support(df,2,20,20)
print(some)

