import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error

def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    mape = mean_absolute_percentage_error(y_test, predictions) * 100
    
    print(f'RMSE: {rmse}')
    print(f'MAPE: {mape:.2f}%')
    
    plt.figure(figsize=(14, 7))
    plt.plot(y_test, label='Actual Price', color='blue')
    plt.plot(predictions, label='Predicted Price', color='orange')
    plt.title('Actual vs Predicted Stock Price')
    plt.xlabel('Time')
    plt.ylabel('Stock Price')
    plt.legend()
    plt.grid(True)
    plt.show()
