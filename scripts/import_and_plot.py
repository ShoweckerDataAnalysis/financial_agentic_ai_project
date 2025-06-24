import subprocess
import sys
import os
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

    output_dir = "/data/shared"
    os.makedirs(output_dir, exist_ok=True)

    # 🔁 Clear old PNG files from the directory
    for file in os.listdir(output_dir):
        if file.endswith(".png"):
            try:
                os.remove(os.path.join(output_dir, file))
                print(f"🗑️ Deleted old file: {file}")
            except Exception as e:
                print(f"⚠️ Could not delete file {file}: {e}")
    
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
        
        # Save the plot to shared folder with name and datetime
        filename = f"{name.replace(' ', '_')}_{run_time}.png"
        filepath = os.path.join(output_dir, filename)
        plt.savefig(filepath)
        plt.close()
        print(f"✅ Saved plot: {filepath}")
        
    return data

# ==== User-editable section ====
tickers = {
    "Google": "GOOG",
    "Apple": "AAPL",
    "Oil": "CL=F"
}

period = "1y"       # e.g. 90d, 1y, 6mo
interval = "1d"     # e.g. 1d, 1wk, 1mo

# ==== Main execution ====
if __name__ == "__main__":
    print("📊 Fetching and plotting data...")
    data = fetch_and_plot_individual(tickers, period, interval)