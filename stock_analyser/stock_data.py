import yfinance as yf





def stock_hist(stock,interval, start, end):
    stock_name = yf.Ticker(stock)
    history = stock_name.history(start=start, end=end, interval=interval)
    return history


def stock_hist2(stock, interval, period):
    stock_name = yf.Ticker(stock)
    history = stock_name.history(period=period, interval = interval)
    return history['Close'][-1]