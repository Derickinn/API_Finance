import requests
import os

API_BR_KEY = os.getenv("BRAPI_TOKEN")
url_br = f"https://brapi.dev/api/quote/{{ticker}}"


def buscar_ticker_stock(ticker):

    url = f"https://brapi.dev/api/quote/{ticker}"

    resposta = requests.get(url)

    print("Status:", resposta.status_code)
    print("Resposta:", resposta.json())

buscar_ticker_stock("AAPL")  # Exemplo de uso da função com o ticker "AAPL"