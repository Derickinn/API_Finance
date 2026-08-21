import requests
import os
from dotenv import load_dotenv

load_dotenv()

url = "https://api.twelvedata.com/symbol_search"

API_KEY = os.getenv("TWELVE_DATA_KEY")

params = {

    "symbol": "MXRF11",
    "apikey": API_KEY
}

resposta = requests.get(url, params=params)

print(resposta.status_code)
print(resposta.json())