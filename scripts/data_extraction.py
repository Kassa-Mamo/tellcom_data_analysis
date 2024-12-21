import pandas as pd

def extract_features(df):
    """Extract relevant features for analysis."""
    
    # Convert timestamp to datetime if necessary
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
    
    # Example: Extracting date and call duration from timestamp and 'call_duration' columns
    df['call_date'] = df['timestamp'].dt.date
    df['call_duration'] = pd.to_numeric(df['call_duration'], errors='coerce')
    
    # Extract day of the week and hour from timestamp
    df['day_of_week'] = df['timestamp'].dt.dayofweek
    df['hour_of_day'] = df['timestamp'].dt.hour
    
    # Derived feature: call duration in minutes
    df['call_duration_minutes'] = df['call_duration'] / 60
    
    # If 'call_type' exists, encode it
    if 'call_type' in df.columns:
        df['call_type_encoded'] = df['call_type'].astype('category').cat.codes
    
    # Drop rows with invalid data
    df.dropna(subset=['timestamp', 'call_duration'], inplace=True)
    
    return df

# Example usage
if __name__ == "__main__":
    data = pd.read_excel(r"C:\Users\user\Desktop\10 acadamey - W 2\tellcom_data_analysis\Data\Week2_challenge_data_source.xlsx")
    extracted_data = extract_features(data)
    print(extracted_data.head())
