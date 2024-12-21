import pandas as pd

def clean_data(df):
    """Clean the dataset."""
    
    # Handle missing values by filling with mean (for numeric columns)
    df.fillna(df.mean(), inplace=True)
    
    # Drop rows with missing critical columns (e.g., timestamp or call_duration)
    df.dropna(subset=['timestamp', 'call_duration'], inplace=True)
    
    # Remove duplicate rows
    df.drop_duplicates(inplace=True)
    
    # Example: Remove outliers in 'call_duration' by setting a threshold
    df = df[df['call_duration'] < df['call_duration'].quantile(0.95)]
    
    return df

# Example usage
if __name__ == "__main__":
    # Load data from Excel (adjust path as needed)
    data = pd.read_excel(r"C:\Users\user\Desktop\10 acadamey - W 2\tellcom_data_analysis\Data\Week2_challenge_data_source.xlsx")
    
    # Clean data
    cleaned_data = clean_data(data)
    print(cleaned_data.head())
