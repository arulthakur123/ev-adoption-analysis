import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Load cleaned EV data
ev_df = pd.read_csv("cleaned_ev_state_data.csv")
ev_df['state_name'] = ev_df['state_name'].str.strip().str.lower()

# Load India states GeoJSON
geo = gpd.read_file("india_states.geojson")
print("✅ GeoJSON file loaded successfully.")
print("📄 Available columns in GeoJSON:\n", geo.columns.tolist())

# Normalize state name column
geo['state_name'] = geo['NAME_1'].str.strip().str.lower()

# Merge EV data with geospatial data
merged = geo.merge(ev_df, on='state_name', how='left')

# --- Static Map: Total EVs ---
fig, ax = plt.subplots(1, 1, figsize=(12, 10))
merged.plot(column='grand_total', cmap='viridis', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
ax.set_title("Total EV Adoption Across Indian States", fontsize=15)
ax.axis("off")
plt.tight_layout()
plt.savefig("map_ev_adoption.png")
print("🖼️ Static map saved as map_ev_adoption.png")

# --- Interactive Map: Charging Stations ---
fig_plotly = px.choropleth(
    merged,
    geojson=merged.geometry.__geo_interface__,
    locations=merged.index,
    color="total_charging_stations",
    hover_name="state_name",
    color_continuous_scale="Plasma",
    title="🔌 Total EV Charging Stations by State",
)
fig_plotly.update_geos(fitbounds="locations", visible=False)
fig_plotly.write_html("map_charging_stations.html")
print("🌐 Interactive map saved as map_charging_stations.html")
