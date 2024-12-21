import pandas as pd

# Assuming you have a DataFrame called 'data'
user_summary = data.groupby('user_id').agg(
    number_of_sessions=('session_id', 'count'),
    session_duration=('session_duration', 'sum'),
    total_dl_data=('download_data', 'sum'),
    total_ul_data=('upload_data', 'sum'),
    total_data_volume=('data_volume', 'sum')
)
