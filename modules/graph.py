import matplotlib.pyplot as plt
import pandas as pd
from io import BytesIO
import base64

plt.switch_backend('agg')

def plot_comments(df=None):
    """Plots the number of comments over time."""

    # Convert the "date" column to datetime objects
    df['date'] = pd.to_datetime(df['date'])

    # Set the "date" column as the index
    df.set_index('date', inplace=True)

    # Resample data over a specific time interval, e.g., daily
    resampled = df.resample('D').size()

    # Create the plot for all data
    plt.figure(figsize=(18, 12))
    plt.bar(resampled.index, resampled.values, color='#30D5C7', label='All Data')
    plt.xlabel("Date", fontsize=20)
    plt.ylabel("Number of comments", fontsize=20)
    plt.title("Comment Count Over Time", fontsize=26)
    plt.xticks(rotation=30)
    plt.legend()

    plt.tight_layout(pad=2) 

    # Create the plot for the last 7 days of data
    last_7_days = resampled.index[:7]
    last_7_days_data = resampled[:7]
    plt.figure(figsize=(20, 12))
    plt.plot(last_7_days, last_7_days_data.values, marker='o', color='#30D5C7', linestyle='-', label='Last 7 Days')
    plt.xlabel("Date (First 7 Days)", fontsize=20)
    plt.ylabel("Number of Comments", fontsize=20)
    plt.title("Comment Count Over the First 7 Days", fontsize=26)
    plt.xticks(rotation=30)
    plt.legend()  
    plt.tight_layout(pad=1.5) 

    buffer1 = BytesIO()
    plt.savefig(buffer1, format='png')
    buffer1.seek(0)

    plt.figure(1)  # Switch back to the first figure

    buffer2 = BytesIO()
    plt.savefig(buffer2, format='png')
    buffer2.seek(0)

    # Encode the BytesIO objects in base64
    graph1 = base64.b64encode(buffer1.read()).decode()
    graph2 = base64.b64encode(buffer2.read()).decode()

    return graph1, graph2

# Example usage:
# graph1, graph2 = plot_comments(df)





