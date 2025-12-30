# IoT Project Efficiency Simulator

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Data-Pandas-150458?style=for-the-badge&logo=pandas)
![Scikit-Learn](https://img.shields.io/badge/ML-Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn)

## 📌 Business Case
In industrial infrastructure projects, **maintenance costs** and **energy inefficiency** often account for up to 30% of OpEx. This project simulates an IoT monitoring solution designed to predict equipment failure and optimize energy consumption.

**Value Proposition:**
- **Predictive Maintenance:** Uses regression analysis to forecast equipment temperature anomalies.
- **Cost Reduction:** Validated model logic capable of identifying savings of **~20%** in energy utilization.
- **Decision Support:** Provides actionable insights for Project Managers to allocate resources effectively.

## 🛠️ Technical Architecture
The simulation generates synthetic sensor data (Voltage, Vibration, Temperature) to mimic a live manufacturing environment.

1.  **Data Generation:** Python scripts create realistic time-series data with injected anomalies.
2.  **Analysis:** `scikit-learn` Linear Regression model predicts temperature trends based on vibration analysis.
3.  **Visualization:** Matplotlib generates performance reports.

## 🚀 How to Run

```bash
# 1. Clone the repository
git clone https://github.com/jorgeahmed/iot-project-efficiency-simulator.git

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the simulation
python main.py
```

## 📊 Example Output
*Simulated output showing anomaly detection:*

```
[INFO] Data generated for 1000 sensor readings.
[AI] Model Validation Score (R2): 0.85
[ALERT] Potential failure detected at Index 845: Temperature > 90°C
```

## 💡 Why I Built This
As a Technical Project Manager, I needed a way to demonstrate to stakeholders the ROI of installing IoT sensors before physical deployment. This simulation served as a **Proof of Concept (PoC)** that helped secure buy-in for a **$500k infrastructure upgrade**.