# Advanced Logistics Data Analysis
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)
# Simulate 1,200 shipments with realistic logistics relationships.
# (Full report contains the complete generated dataset and methodology.)

df = pd.read_csv("hypothetical_logistics_dataset.csv", parse_dates=["Date"])

numeric_cols = [
    "Shipment_Volume_tons", "Distance_km", "Delivery_Time_days",
    "Transport_Cost_USD", "Delay_Days", "Cost_per_ton_USD"
]

print(df[numeric_cols].describe())
print(df[numeric_cols].corr())

mode_perf = df.groupby("Transport_Mode").agg(
    On_Time_Rate=("On_Time", "mean"),
    Avg_Delivery_Days=("Delivery_Time_days", "mean"),
    Avg_Cost_USD=("Transport_Cost_USD", "mean")
)

# Distribution
plt.figure(figsize=(8.5, 5))
plt.hist(df["Delivery_Time_days"], bins=30, edgecolor="black")
plt.title("Distribution of Delivery Time")
plt.xlabel("Delivery time (days)")
plt.ylabel("Shipments")
plt.show()

# Category comparison
rate = df.groupby("Transport_Mode")["On_Time"].mean().sort_values()
plt.figure(figsize=(8.5, 5))
plt.barh(rate.index, rate.values * 100)
plt.title("On-Time Delivery Rate by Transport Mode")
plt.xlabel("On-time rate (%)")
plt.show()

# Relationship analysis
for mode in ["Road", "Rail", "Air"]:
    s = df[df["Transport_Mode"] == mode]
    plt.scatter(
        s["Distance_km"], s["Transport_Cost_USD"],
        s=s["Shipment_Volume_tons"] * 4, alpha=0.45, label=mode
    )
plt.title("Transportation Cost vs Distance")
plt.xlabel("Distance (km)")
plt.ylabel("Cost (USD)")
plt.legend()
plt.show()
