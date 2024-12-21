import pandas as pd

def form_data(df):
    """Transform the data into the desired format."""
    
    # Example: Grouping by 'call_date' and summing up 'call_duration'
    grouped_data = df.groupby('call_date')['call_duration'].sum().reset_index()
    
    # Example: Pivot the data if needed
    pivot_data = df.pivot_table(values='call_duration', index='call_date', columns='call_type', aggfunc='sum')
    
    return grouped_data, pivot_data

# Example usage
if __name__ == "__main__":
    data = pd.read_excel(r"C:\Users\user\Desktop\10 acadamey - W 2\tellcom_data_analysis\Data\Week2_challenge_data_source.xlsx")
    grouped_data, pivot_data = form_data(data)
    print(grouped_data.head())
    print(pivot_data.head())
