import yfinance as yf

#define the ticker symbol
tickerSymbol = "AAPL"

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2022-08-23', end='2022-08-23')

#see your data
# print(tickerDf.tail())
for row in tickerDf.iterrows():
    print (row[2])

# import pandas as pd
# import requests
# from dotenv import load_dotenv
# import os

# load_dotenv()

# API_KEY = os.environ.get('API_KEY')


# def get_intraday_data(symbol, interval):
#     # API_KEY = open(r'api_key.txt')
#     api_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval={interval}&apikey={API_KEY}'
#     raw_df = requests.get(api_url).json()
#     df = pd.DataFrame(raw_df[f'Time Series ({interval})']).T
#     df = df.rename(columns = {'1. open': 'open', '2. high': 'high', '3. low': 'low', '4. close': 'close', '5. volume': 'volume'})
#     for i in df.columns:
#         df[i] = df[i].astype(float)
#     df.index = pd.to_datetime(df.index)
#     df = df.iloc[::-1]
#     return df

# tsla_intra = get_intraday_data('NSI:WIPRO', '1min')
# print(tsla_intra.tail())