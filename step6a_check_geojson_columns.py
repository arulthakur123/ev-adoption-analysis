import geopandas as gpd
import sys

try:
    geo = gpd.read_file("india_states.geojson")
    print("\n✅ GeoJSON file loaded successfully.")
    print("📄 Available columns in GeoJSON:\n", geo.columns.tolist())
except Exception as e:
    print("❌ Error loading GeoJSON file:", e)

sys.stdout.flush()
