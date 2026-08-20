import requests, os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ALPHA_VANTAGE_KEY")

url = "https://www.alphavantage.co/query"

params = {

    "function": "TIME_SERIES_DAILY",
    "symbol": "AAPL",
    "interval": "5min",
    "apikey": API_KEY

}
