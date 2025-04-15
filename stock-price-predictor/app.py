import streamlit as st
import pandas as pd
from tensorflow.keras.models import load_model
from data_loader.yahoo_finance import load_stock_data
from utils.preprocessing import preprocess_data
from visualization.plot_data import plot_close_ma, plot_rsi, plot_daily_return
from utils.evaluate_model import evaluate_model
import numpy as np

model = load_model('saved_models/lstm_stock_model.h5', compile=False)

st.title("AI Powered Stock Price Predictor 📈")
st.markdown("Built with LSTM & Yahoo Finance API")

stock_symbol = st.text_input("Enter Stock Symbol (Example: AAPL, TSLA, INFY)")

if stock_symbol:
    df = load_stock_data(stock_symbol, '2020-01-01', '2024-04-01')
    df = preprocess_data(df)
    
    st.subheader("Stock Data Overview")
    st.write(df.tail())

    st.subheader("Price & Technical Indicators")
    plot_close_ma(df)
    plot_rsi(df)
    plot_daily_return(df)

    features = df[['Open', 'High', 'Low', 'Close', 'Volume', 'MA20', 'MA50', 'EMA', 'RSI']].values
    window_size = 60
    X = []

    for i in range(window_size, len(features)):
        X.append(features[i-window_size:i])

    X = np.array(X)

    st.subheader("Prediction vs Actual Price")
    evaluate_model(model, X, df['Close'][window_size:].values)

st.markdown("---")
st.write("Made with ❤️ by Kartikay Kant")
