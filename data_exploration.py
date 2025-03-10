import pandas as pd

# Load the dataset with the correct filename and path
file_path = "/Users/pastorbobby/Medical_Trend_Analysis/Faulty Medical Devices.csv"

# Read the CSV file
df = pd.read_csv(file_path)

# Display basic information about the dataset
print("Dataset Information:")
print(df.info())

# Display the first few rows of the dataset
print("\nFirst 5 rows:")
print(df.head())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Summary statistics of numerical columns
print("\nSummary Statistics:")
print(df.describe())

# Check for duplicate rows
duplicates = df.duplicated().sum()
print(f"\nNumber of duplicate rows: {duplicates}")

# Display column names
print("\nColumn Names:")
print(df.columns)