import random
import time
import sqlite3

# Connect to SQLite DB (local storage)
conn = sqlite3.connect("energy_management.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS resource_usage (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    energy_kwh REAL,
    water_liters REAL
)
""")

# Simulate sensor data
for _ in range(10):  # simulate 10 readings
    energy = round(random.uniform(1.0, 5.0), 2)   # kWh
    water = round(random.uniform(10.0, 50.0), 2) # liters
    
    cursor.execute("INSERT INTO resource_usage (energy_kwh, water_liters) VALUES (?, ?)", (energy, water))
    conn.commit()
    time.sleep(1)

print("Sample data inserted successfully!")
conn.close()
