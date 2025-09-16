from flask import Flask, render_template_string
import sqlite3
import pandas as pd

app = Flask(__name__)

@app.route("/")
def dashboard():
    conn = sqlite3.connect("energy_management.db")
    df = pd.read_sql_query("SELECT * FROM resource_usage ORDER BY id DESC LIMIT 5", conn)
    conn.close()
    
    html = """
    <h1>Energy & Resource Management Dashboard</h1>
    <table border="1" cellpadding="5">
        <tr><th>ID</th><th>Timestamp</th><th>Energy (kWh)</th><th>Water (Liters)</th></tr>
        {% for row in data %}
        <tr><td>{{row.id}}</td><td>{{row.timestamp}}</td><td>{{row.energy_kwh}}</td><td>{{row.water_liters}}</td></tr>
        {% endfor %}
    </table>
    """
    return render_template_string(html, data=df.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
