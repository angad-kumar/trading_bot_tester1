import hist_data.hist_data as hist
import pandas as pd
from finta import TA
import numpy as np



def chandelier_exit(stock, interval , period):
    data = hist.stock_hist2(stock,interval,period)
    data.rename(columns={"Close": 'close', "High": 'high', "Low": 'low', 'Volume': 'volume', 'Open': 'open'}, inplace=True)

    # results = indicators.get_chandelier(data, 22, 3)
    df = pd.DataFrame(data)
    t = df['close']
    df = TA.CHANDELIER(df)

    df['close'] = t

    df['Buy'] = np.where(df['Short.'] < df['close'], 'True', 'False')
    df['Sell'] = np.where(df['Long.'] > df['close'], 'True', 'False')
    # print(df['Sell'][-1])
    
    if(df['Sell'][-1] == 'False'):
        return "Buy"

    elif(df['Sell'][-1] == 'True'):
        return "Sale"
    

# print(chandelier_exit("^NSEI", "15m","1mo"))