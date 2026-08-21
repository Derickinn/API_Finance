import requests, os
from dotenv import load_dotenv    

load_dotenv()

API_KEY = os.getenv("TWELVE_DATA_KEY")
url = "https://api.twelvedata.com/time_series"

API_BR_KEY = os.getenv("BRAPI_TOKEN")

def buscar_ticker_stock():

    ticker = input("Digite o ticker da ação: (Exemplo: AAPL, MSFT, TSLA): ").upper()

    formula_cotacao(ticker)

def buscar_ticker_crypto():

    ticker = input("Digite o ticker da criptomoeda: (Exemplo: BTC, ETH, XRP): ").upper()

    ticker = f"{ticker}/USD"  # Adiciona o sufixo /USD para criptomoedas

    formula_cotacao(ticker)

def formula_cotacao(ticker):

    params = {
    
                "interval": "1min",
                "outputsize": 1,
                "symbol": ticker,
                "apikey": API_KEY
    
            }

    resposta = requests.get(url, params=params)
    dados = resposta.json()
    meta_data = dados["meta"]
    cotacao = float(dados["values"][0]["close"])
    print(f"\nA cotação atual da ação {meta_data['symbol']} é: $ {cotacao:.2f}")
