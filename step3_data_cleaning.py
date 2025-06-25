import pandas as pd

# Load the dataset
df = pd.read_csv("ev_state_data.csv")

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("-", "_")

# Print missing values before cleaning
print("🔍 Missing values before cleaning:")
print(df.isnull().sum())

# Fill missing values in charging stations with 0
df["total_charging_stations"] = df["total_charging_stations"].fillna(0)

# Drop irrelevant column
if "unnamed:_0" in df.columns:
    df.drop(columns=["unnamed:_0"], inplace=True)

# Save cleaned data
df.to_csv("cleaned_ev_state_data.csv", index=False)
print("✅ Data cleaned and saved to cleaned_ev_state_data.csv")
