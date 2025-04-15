import yfinance as yf
import pandas as pd

def load_stock_data(stock_symbol, start_date, end_date):
    stock = yf.Ticker(stock_symbol)
    df = stock.history(start=start_date, end=end_date)
    
    if df.empty:
        print("No Data Found for", stock_symbol)
    else:
        print("Data Loaded Successfully for", stock_symbol)
    
    return df
