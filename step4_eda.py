import matplotlib
matplotlib.use('TkAgg')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv("cleaned_ev_state_data.csv")
sns.set(style="whitegrid")

# 🔹 Chart 1: Top 10 states by total EVs
top_states = df.sort_values(by="grand_total", ascending=False).head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x="grand_total", y="state_name", data=top_states, palette="viridis")
plt.title("🔋 Top 10 States by Total Number of EVs")
plt.xlabel("Total EVs")
plt.ylabel("State")
plt.tight_layout()
plt.savefig("top_10_states_total_evs.png")  # ✅ Save chart 1
plt.show()

# 🔹 Chart 2: Top states by charging stations
charging = df.sort_values(by="total_charging_stations", ascending=False).head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x="total_charging_stations", y="state_name", data=charging, palette="Blues_d")
plt.title("⚡ Top 10 States by EV Charging Stations")
plt.xlabel("Charging Stations")
plt.ylabel("State")
plt.tight_layout()
plt.savefig("top_10_charging_stations.png")  # ✅ Save chart 2
plt.show()

# 🔹 Chart 3: Total EVs vs Charging Stations (Scatter)
plt.figure(figsize=(10, 6))
sns.scatterplot(x="grand_total", y="total_charging_stations", data=df, hue="state_name", palette="hsv", legend=False)
plt.title("📊 Total EVs vs Charging Stations")
plt.xlabel("Total EVs")
plt.ylabel("Charging Stations")
plt.tight_layout()
plt.savefig("evs_vs_charging_stations.png")  # ✅ Save chart 3
plt.show()
