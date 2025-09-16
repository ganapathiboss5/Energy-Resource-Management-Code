import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Load data from DB
conn = sqlite3.connect("energy_management.db")
df = pd.read_sql_query("SELECT * FROM resource_usage", conn)

# Plot energy usage
plt.figure(figsize=(6,4))
plt.plot(df["timestamp"], df["energy_kwh"], marker="o")
plt.title("Energy Consumption Over Time")
plt.xlabel("Timestamp")
plt.ylabel("Energy (kWh)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot water usage
plt.figure(figsize=(6,4))
plt.plot(df["timestamp"], df["water_liters"], marker="s", color="green")
plt.title("Water Consumption Over Time")
plt.xlabel("Timestamp")
plt.ylabel("Water (Liters)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

conn.close()
