import requests, os
from dotenv import load_dotenv
from busca_ticker import buscar_ticker_stock, buscar_ticker_crypto

load_dotenv()

API_KEY = os.getenv("TWELVE_DATA_KEY")

API_BR_KEY = os.getenv("BRAPI_TOKEN")

url = "https://api.twelvedata.com/time_series"

print("\nBem-vindo ao programa de busca de cotações!")

while True:

    print("\nDigite o tipo de ticker que deseja consultar:")

    opcoes = {

        1 : buscar_ticker_stock,
        2 : buscar_ticker_crypto,
        3 : exit

    }

    try:

        escolha = int(input("\n(1) Ações\n(2) Criptomoedas\n(3) Sair\nEscolha uma opção: "))

    except ValueError:

        print("\n🔴 Opção inválida. Por favor, escolha uma opção válida.🔴")

        continue

    funcoes = opcoes.get(escolha)

    if funcoes:

        funcoes()

        print("\nDeseja realizar outra consulta?")

        continuar = input("(1) Sim\n(2) Não\nEscolha uma opção: ").upper()

        if continuar == "2":

            break

        elif continuar == "1":
            
            continue

        else:

            print("\n🔴 Opção inválida. Por favor, escolha uma opção válida.🔴")

    else:

        print("\n🔴 Opção inválida. Por favor, escolha uma opção válida.🔴")

    