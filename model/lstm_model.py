from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

def create_lstm_model(input_shape):
    model = Sequential()
    
    model.add(LSTM(128, return_sequences=True, input_shape=input_shape))
    model.add(Dropout(0.2))
    
    model.add(LSTM(64, return_sequences=False))
    model.add(Dropout(0.2))
    
    model.add(Dense(1))
    
    model.compile(optimizer='adam', loss='mse')
    return model
