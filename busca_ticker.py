import requests, os
from dotenv import load_dotenv    

load_dotenv()

def buscar_ticker_stock():

    ticker = input("Digite o ticker da stock: (Exemplo: AAPL, MSFT, TSLA): ").upper()

    meta_data, cotacao = formula_cotacao(ticker)

    print(f"\nA cotação atual do stock {meta_data['symbol']} é: $ {cotacao:.2f}")

def buscar_ticker_crypto():

    ticker = input("Digite o ticker da criptomoeda: (Exemplo: BTC, ETH, XRP): ").upper()

    ticker = f"{ticker}/USD"  # Adiciona o sufixo /USD para criptomoedas

    meta_data, cotacao = formula_cotacao(ticker)

    print(f"\nA cotação atual da criptomoeda {meta_data['symbol']} é: $ {cotacao:.2f}")

def buscar_ticker_br():

    ticker = input("Digite o ticker da ação: (Exemplo: BBAS3, VALE3, ITUB4): ").upper()

    meta_data, cotacao = formula_cotacao_br(ticker)

    print(f"\nA cotação atual da ação {meta_data['symbol']} é: $ {cotacao:.2f}")

def buscar_ticker_fii():

    ticker = input("Digite o ticker do FII: (Exemplo: HGLG11, VISC11, JPPA11): ").upper()
    
    meta_data, cotacao = formula_cotacao_br(ticker)

    print(f"\nA cotação atual do FII {meta_data['symbol']} é: $ {cotacao:.2f}")

def formula_cotacao(ticker):

    API_KEY = os.getenv("TWELVE_DATA_KEY")

    url = "https://api.twelvedata.com/time_series"

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

    return meta_data, cotacao

def formula_cotacao_br(ticker):

    url_br = f"https://brapi.dev/api/quote/{ticker}"

    API_BR_KEY = os.getenv("BRAPI_TOKEN")

    params = {

                "symbols": ticker,
                "regularMarketPrice": "regularMarketPrice",
                "token": API_BR_KEY

            }
    
    resposta = requests.get(url_br, params=params)

    dados = resposta.json()

    resultado = dados["results"][0]

    return resultado, float(resultado.get("regularMarketPrice"))
