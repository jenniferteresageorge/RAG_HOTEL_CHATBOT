import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from .data_loader import load_data

df = load_data()

def revenue_trend():
    revenue = df.groupby(df['reservation_status_date'].dt.to_period("M"))['revenue'].sum()
    revenue.plot(kind='line', title="Monthly Revenue Trend")
    plt.show()
    return revenue.to_dict()

def cancellation_rate():
    rate = (df['is_canceled'].sum() / len(df)) * 100
    return {"cancellation_rate": rate}

def geographical_distribution():
    location_counts = df['country'].value_counts()
    return location_counts.to_dict()

def lead_time_distribution():
    return df['lead_time_days'].describe().to_dict()
