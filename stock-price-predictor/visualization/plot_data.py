import matplotlib.pyplot as plt
import seaborn as sns

def plot_close_ma(df):
    plt.figure(figsize=(14, 7))
    plt.plot(df['Close'], label='Close Price', color='blue')
    plt.plot(df['MA20'], label='MA 20', color='orange')
    plt.plot(df['MA50'], label='MA 50', color='green')
    plt.title('Close Price with Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_rsi(df):
    plt.figure(figsize=(14, 4))
    plt.plot(df['RSI'], color='purple')
    plt.axhline(70, linestyle='--', color='red')
    plt.axhline(30, linestyle='--', color='green')
    plt.title('Relative Strength Index (RSI)')
    plt.xlabel('Date')
    plt.ylabel('RSI Value')
    plt.grid(True)
    plt.show()

def plot_daily_return(df):
    plt.figure(figsize=(10, 5))
    sns.histplot(df['Daily Return'], bins=50, color='purple')
    plt.title('Distribution of Daily Returns')
    plt.xlabel('Daily Return')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()
