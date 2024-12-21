import pandas as pd
import matplotlib.pyplot as plt

# Load the data (make sure the correct file path is provided)
file_path = 'your_file_path_here.xlsx'  # Replace this with your actual file path
data = pd.read_excel(file_path)

# Check if 'session_duration' is a column in the DataFrame
if 'session_duration' in data.columns:
    # Plot a histogram of the session_duration column
    plt.hist(data['session_duration'], bins=20)
    plt.title('Histogram of Session Duration')
    plt.xlabel('Session Duration')
    plt.ylabel('Frequency')
    plt.show()
else:
    print("Error: 'session_duration' column not found in the data.")

# Display the first few rows of the DataFrame to confirm the data structure
print("First 5 rows of the data:")
print(data.head())

# Display basic statistics of the data
print("\nBasic Stats of the Data:")
print(data.describe())
