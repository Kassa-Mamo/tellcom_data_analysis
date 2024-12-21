import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# File paths for your data
week2_data_path = r"C:\Users\user\Desktop\10 acadamey - W 2\tellcom_data_analysis\Data\Week2_challenge_data_source.xlsx"
field_desc_path = r"C:\Users\user\Desktop\10 acadamey - W 2\tellcom_data_analysis\Data\Field Description.xlsx"

# Load the data
try:
    week2_data = pd.read_excel(week2_data_path, engine="openpyxl")
    field_description = pd.read_excel(field_desc_path, engine="openpyxl")
    print("Data loaded successfully!")
except Exception as e:
    print(f"Error loading data: {e}")

# Display the first few rows of both dataframes
print("Week 2 Data Head:\n", week2_data.head())
print("Field Description Head:\n", field_description.head())

# Check if the 'Outputs/interim_plots' directory exists, if not, create it
if not os.path.exists("Outputs/interim_plots"):
    os.makedirs("Outputs/interim_plots")

# Replace empty strings with NaN in the dataset to handle missing values properly
week2_data.replace('', pd.NA, inplace=True)

# Check for missing data in the week2_data
missing_data = week2_data.isna().sum()
print("Missing Data:\n", missing_data)

# Select only numeric columns
numeric_columns = week2_data.select_dtypes(include=['number'])

# Fill missing values with the mean of each numeric column
numeric_columns.fillna(numeric_columns.mean(), inplace=True)

# Replace the numeric columns in the original dataframe
week2_data[numeric_columns.columns] = numeric_columns

# Optionally: Drop rows with any NaN values (if you'd like to drop non-numeric missing values)
# week2_data.dropna(inplace=True)

# Convert columns to numeric (coerce non-numeric to NaN)
week2_data = week2_data.apply(pd.to_numeric, errors='coerce')

# Check the cleaned data
print("Cleaned Data Head:\n", week2_data.head())

# Correlation matrix for visualizing relationships between variables
corr_matrix = week2_data.corr()

# Plot the correlation matrix as a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix")
plt.savefig("Outputs/interim_plots/correlation_matrix.png")  # Save plot
plt.show()

# Scatter plot between two columns (replace 'column_1' and 'column_2' with actual column names)
# Example: column_1 = 'Revenue', column_2 = 'Expenditure' (make sure to replace with actual column names)
plt.figure(figsize=(8, 6))
sns.scatterplot(data=week2_data, x='column_1', y='column_2')  # Replace with actual column names
plt.title("Scatter Plot of column_1 vs column_2")
plt.xlabel("column_1")
plt.ylabel("column_2")
plt.savefig("Outputs/interim_plots/scatter_plot.png")  # Save plot
plt.show()

# Process data in chunks (if dataset is large)
chunk_size = 10000
for chunk in pd.read_excel(week2_data_path, engine="openpyxl", chunksize=chunk_size):
    print(chunk.head())  # Process each chunk (e.g., print first few rows)

# Optionally: Save the cleaned data to a new Excel file for future use
cleaned_data_path = r"C:\Users\user\Desktop\10 acadamey - W 2\tellcom_data_analysis\Data\Cleaned_Week2_data.xlsx"
week2_data.to_excel(cleaned_data_path, index=False, engine="openpyxl")
print(f"Cleaned data saved to {cleaned_data_path}")

