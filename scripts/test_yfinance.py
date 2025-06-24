# import subprocess
# import sys

# def install_if_missing(package_name, import_name=None):
#     import_name = import_name or package_name
#     try:
#         __import__(import_name)
#         print(f"{package_name} is already installed.")
#     except ImportError:
#         print(f"{package_name} not found. Installing...")
#         subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

# # Check and install packages
# install_if_missing('matplotlib')
# install_if_missing('pandas')
# install_if_missing('yfinance')

# # Now import them safely
# import matplotlib.pyplot as plt
# import pandas as pd
# import yfinance as yf
# from datetime import datetime

import yfinance as yf

data = yf.download("AAPL", period="1d")
print(data.tail())