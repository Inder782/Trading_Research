import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)

df= pd.read_csv("NIFTY_01-10-2006_to_25-12-2024_1day.csv")

#clean the dataframe
df=df.drop(columns="volume")

# function to identify doji
def doji_finder(df,threshold)->pd.DataFrame:
    
    body = df["close"]-df["open"]
    high_low = df["high"]-df["low"]

    df["Doji_y_n"] = np.where((body / high_low) * 100 < threshold, 1, 0)

    return df

print(doji_finder(df,5))
    

