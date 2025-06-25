import pandas as pd

# Load your dataset
df = pd.read_csv("ev_state_data.csv")  # make sure this file name is correct and in the same folder

# Display first few rows
print(df.head())


# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace('-', '_')

# Show column names
print("\nCleaned Column Names:\n", df.columns.tolist())

# Check if any missing values exist
null_counts = df.isnull().sum()

print("\nMissing values in each column:")
print(null_counts)

# Show total missing entries
total_missing = null_counts.sum()
print(f"\n🔍 Total missing entries in dataset: {total_missing}")
