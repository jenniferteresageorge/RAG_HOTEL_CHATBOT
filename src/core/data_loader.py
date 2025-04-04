import pandas as pd
import os

# Load dataset (modify path as needed)
DATA_PATH = os.path.join(os.path.dirname(__file__), "../../data/hotel_bookings.csv")

def load_data():
    df = pd.read_csv(DATA_PATH)
    
    # Handle missing values
    df.fillna({'agent': 'Unknown', 'company': 'Unknown'}, inplace=True)
    
    # Convert date columns
    df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'])
    
    # Feature Engineering
    df['lead_time_days'] = df['lead_time']
    df['revenue'] = df['adr'] * df['stays_in_week_nights']  # Approx revenue
    
    return df
