import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

# Simulate yearly EV adoption totals (assumed growth from 2015 to 2024)
years = list(range(2015, 2025))
adoption_counts = [50000, 70000, 95000, 130000, 180000, 250000, 310000, 400000, 510000, 588000]  # use grand_total trend

# Build dataframe for Prophet
df_forecast = pd.DataFrame({
    'ds': pd.to_datetime(years, format='%Y'),
    'y': adoption_counts
})

# Prophet model
model = Prophet(yearly_seasonality=True)
model.fit(df_forecast)

# Future prediction for next 5 years
future = model.make_future_dataframe(periods=5, freq='Y')
forecast = model.predict(future)

# Plot forecast
fig1 = model.plot(forecast)
plt.title("EV Adoption Forecast (India) - Total")
fig1.savefig("fig_forecast_total_ev.png")

fig2 = model.plot_components(forecast)
fig2.savefig("fig_forecast_components.png")

print("✅ Forecast generated and saved as images.")
