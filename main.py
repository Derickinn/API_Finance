
from busca_ticker import buscar_ticker_stock, buscar_ticker_crypto, buscar_ticker_br, buscar_ticker_fii

print("\nBem-vindo ao programa de busca de cotações!")

while True:

    print("\nDigite o tipo de ticker que deseja consultar:")

    opcoes = {

        1 : buscar_ticker_stock,
        2 : buscar_ticker_crypto,
        3 : buscar_ticker_br,
        4 : buscar_ticker_fii,
        5 : exit

    }

    try:

        escolha = int(input("\n(1) Ações\n(2) Criptomoedas\n(3) Ações Brasileiras\n(4) FII\n(5) Sair\nEscolha uma opção: "))

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
