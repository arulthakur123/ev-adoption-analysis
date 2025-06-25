import matplotlib.pyplot as plt
import pandas as pd

# Assumptions
initial_cost_ev = 1500000  # EV cost
initial_cost_petrol = 1000000  # Petrol car cost
running_cost_ev_per_km = 8.4 / 10  # ₹8.4 per kWh, 10 km/kWh
running_cost_petrol_per_km = 110 / 18  # ₹110/litre, 18 km/l
km_per_year = 15000
battery_replacement_year = 8
battery_replacement_cost = 350000

# Yearly calculations
years = list(range(1, 11))
ev_costs = []
petrol_costs = []

ev_total = initial_cost_ev
petrol_total = initial_cost_petrol

for year in years:
    ev_running = running_cost_ev_per_km * km_per_year
    petrol_running = running_cost_petrol_per_km * km_per_year

    ev_total += ev_running
    petrol_total += petrol_running

    if year == battery_replacement_year:
        ev_total += battery_replacement_cost

    ev_costs.append(ev_total)
    petrol_costs.append(petrol_total)

# Create DataFrame for analysis
df = pd.DataFrame({
    "Year": years,
    "EV Total Cost": ev_costs,
    "Petrol Total Cost": petrol_costs,
    "Savings (Petrol - EV)": [p - e for p, e in zip(petrol_costs, ev_costs)]
})

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(df["Year"], df["EV Total Cost"], label="EV Total Cost", marker='o')
plt.plot(df["Year"], df["Petrol Total Cost"], label="Petrol Total Cost", marker='o')
plt.xlabel("Year")
plt.ylabel("Total Cost (₹)")
plt.title("EV vs Petrol Total Cost (with Battery Replacement & Infra Cost)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("step7_ev_vs_petrol_cost_realistic.png")
plt.show()

# Print insights
breakeven_year = df[df["Savings (Petrol - EV)"] > 0].iloc[0]["Year"] if not df[df["Savings (Petrol - EV)"] > 0].empty else "Never"
total_savings = df.iloc[-1]["Savings (Petrol - EV)"]
print("\n💡 Cost-Benefit Summary (Realistic):")
print(f"✅ Break-even year for EV vs Petrol: Year {breakeven_year}")
print(f"💰 Total Savings in 10 years: ₹{int(total_savings):,}")
