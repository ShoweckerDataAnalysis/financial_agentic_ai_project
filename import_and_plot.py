import subprocess
import sys
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

# Ensure yfinance is installed
try:
    import yfinance as yf
except ImportError:
    print("yfinance not found. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "yfinance"])
    import yfinance as yf

def fetch_and_plot_individual(tickers, period="90d", interval="1d"):
    """
    Fetch historical data for tickers and save individual closing price plots.
    
    Args:
        tickers (dict): dict of {name: ticker_symbol}
        period (str): period string for yfinance, e.g. '90d', '1y'
        interval (str): data interval, e.g. '1d', '1wk', '1mo'
    """
    data = {}
    run_time = datetime.now().strftime("%Y%m%d_%H%M%S")  # e.g. 20250622_164530
    
    for name, symbol in tickers.items():
        # Download data and reset index for 'Date' column
        df = yf.download(symbol, period=period, interval=interval).reset_index()
        df['Date'] = pd.to_datetime(df['Date'])
        data[name] = df
        
        # Plotting individual ticker
        plt.figure(figsize=(12, 6))
        plt.plot(df['Date'].values, df['Close'].values, label=name, marker='o')
        plt.title(f"{name} Closing Prices ({period})")
        plt.xlabel("Date")
        plt.ylabel("Price (USD)")
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.grid(True)
        
        # Save the plot with name and datetime
        filename = f"{name.replace(' ', '_')}_{run_time}.png"
        plt.savefig(filename)
        plt.close()
        print(f"Saved plot: {filename}")
        
    return data

# ==== User-editable section ====
tickers = {
    "Google": "GOOG",
    "Apple": "AAPL",
    "Oil": "CL=F"
}

period = "1y"   # e.g. 90d, 1y, 6mo
interval = "1d"   # e.g. 1d, 1wk, 1mo

# ==== Main execution ====
if __name__ == "__main__":
    print("Fetching and plotting data...")
    data = fetch_and_plot_individual(tickers, period, interval)