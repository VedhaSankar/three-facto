#from numpy import _2Tuple
import numpy
import yfinance as yf

TICKER_LIST = ['TSLA','AMZN','AAPL','w','AMD']
#define the ticker symbol
def get_low_value(tickerSymbol):

    # tickerSymbol = "AAPL"

    #get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)

    #get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start='2022-08-23', end='2022-08-23')
        



    # Use getitem ([]) to iterate over columns in pandas DataFrame
    #for column in tickerDf:
        #print(tickerDf[column].values)
    l=tickerDf['Low'].values[0]
    return l

def get_all_low_values():

    for ticker in TICKER_LIST:
        print(get_low_value(ticker))
    
    pass
if __name__ =='__main__':
     get_all_low_values()
