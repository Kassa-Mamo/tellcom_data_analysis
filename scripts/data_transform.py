import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

def normalize_data(df):
    """Normalize numeric features."""
    scaler = MinMaxScaler()
    df[['call_duration']] = scaler.fit_transform(df[['call_duration']])
    return df

def standardize_data(df):
    """Standardize numeric features."""
    scaler = StandardScaler()
    df[['call_duration']] = scaler.fit_transform(df[['call_duration']])
    return df

def encode_data(df):
    """Encode categorical features."""
    if 'call_type' in df.columns:
        df['call_type_encoded'] = df['call_type'].astype('category').cat.codes
    return df

# Example usage
if __name__ == "__main__":
    data = pd.read_excel(r"C:\Users\user\Desktop\10 acadamey - W 2\tellcom_data_analysis\Data\Week2_challenge_data_source.xlsx")
    normalized_data = normalize_data(data)
    standardized_data = standardize_data(normalized_data)
    encoded_data = encode_data(standardized_data)
    print(encoded_data.head())
