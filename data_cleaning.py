import pandas as pd

# File Path
file_path = "/Users/pastorbobby/Medical_Trend_Analysis/Faulty Medical Devices.csv"

# Load dataset
df = pd.read_csv(file_path)

# Standardize column names (remove spaces & lowercase)
df.columns = df.columns.str.strip().str.lower()

# Display initial missing values
print("\nInitial Missing Values:\n", df.isnull().sum())

# Drop columns with too many missing values (threshold: 70% missing)
threshold = 0.7 * len(df)
df = df.dropna(thresh=threshold, axis=1)

# Fill missing values safely
df['description'] = df['description'].fillna("No Description")
df['name'] = df['name'].fillna("Unknown")

# Check if 'risk_class' exists before modifying it
if 'risk_class' in df.columns:
    df['risk_class'] = df['risk_class'].fillna("Not Specified")

if 'country' in df.columns:
    df['country'] = df['country'].fillna("Unknown")

# Convert date columns if they exist
for col in ['created_at', 'updated_at']:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')

# Convert quantity_in_commerce to numeric if it exists
if 'quantity_in_commerce' in df.columns and df['quantity_in_commerce'].dtype == object:
    df['quantity_in_commerce'] = pd.to_numeric(df['quantity_in_commerce'], errors='coerce')

# Standardize categorical values
if 'risk_class' in df.columns:
    df['risk_class'] = df['risk_class'].str.strip().str.title()

if 'country' in df.columns:
    df['country'] = df['country'].str.strip().str.title()

# Drop duplicate rows
df = df.drop_duplicates()

# Final missing values count
print("\nFinal Missing Values After Cleaning:\n", df.isnull().sum())

# Save cleaned data
cleaned_file_path = "/Users/pastorbobby/Medical_Trend_Analysis/Cleaned_Faulty_Medical_Devices.csv"
df.to_csv(cleaned_file_path, index=False)

print("\nData Cleaning Complete. Cleaned file saved as:", cleaned_file_path)