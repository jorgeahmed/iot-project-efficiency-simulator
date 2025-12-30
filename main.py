import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

def generate_sensor_data(n=1000):
    """
    Generates synthetic IoT sensor data:
    - Vibration: Random normal distribution
    - Voltage: Stable with minor fluctuations
    - Temperature: Correlated with vibration + random noise
    """
    np.random.seed(42)
    vibration = np.random.normal(50, 10, n)
    voltage = np.random.normal(220, 2, n)
    # Temperature increases with vibration
    temperature = 25 + (0.5 * vibration) + np.random.normal(0, 2, n)
    
    # Inject anomalies
    temperature[845:850] += 50 # Overheating event
    
    df = pd.DataFrame({
        'vibration': vibration,
        'voltage': voltage,
        'temperature': temperature
    })
    return df

def train_predictive_model(df):
    """
    Trains a simple regression model to predict temperature based on vibration.
    Simulates "Digital Twin" predictive capability.
    """
    X = df[['vibration']]
    y = df['temperature']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    score = model.score(X_test, y_test)
    print(f"[AI] Model Validation Score (R2): {score:.2f}")
    
    return model

def check_health(df, threshold=90):
    """
    Simulates real-time monitoring.
    """
    anomalies = df[df['temperature'] > threshold]
    if not anomalies.empty:
        print(f"[ALERT] Potential failure detected at {len(anomalies)} data points.")
        print(f"        Critical Indices: {anomalies.index.tolist()[:5]}...")
    else:
        print("[INFO] System operating within normal parameters.")

if __name__ == "__main__":
    print("--- Starting IoT Efficiency Simulation ---")
    data = generate_sensor_data()
    print(f"[INFO] Data generated for {len(data)} sensor readings.")
    
    model = train_predictive_model(data)
    
    print("[INFO] Running diagnostics...")
    check_health(data)
    
    print("--- Simulation Complete ---")
