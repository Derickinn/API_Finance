import psycopg
import requests, os
from dotenv import load_dotenv    

load_dotenv()

def conectar_bd():

    try:

        conn = psycopg.connect(

            host=os.getenv("Postgres_HOST"),
            port=os.getenv("Postgres_PORT"),
            dbname=os.getenv("Postgres_DB"),
            user=os.getenv("Postgres_USER"),
            password=os.getenv("Postgres_SENHA")

        )

        return conn

    except Exception as e:

        print(f"Erro ao conectar ao banco de dados: {e}")

        return None

def visualizar_ativos():

    with conectar_bd() as conn:

        with conn.cursor() as cur:

            cur.execute("SELECT * FROM ativos;")

            ativos = cur.fetchall()

            if len(ativos) == 0:

                print("\nNão existem ativos salvos! tente adicionar algum primeiro")

                return

            for ativo in ativos:

                print(ativo)

def cadastrar_ativo(ticker, tipo, preco):

    if tipo == "stock" or tipo == "ação" or tipo == "cripto":

        with conectar_bd() as conn:

            with conn.cursor() as cur:

                cur.execute("INSERT INTO ativos (ticker, tipo, preco) values (%s, %s, %s)", (ticker, tipo, preco))

                conn.commit()

    if tipo == "Fii" :

        with conectar_bd() as conn:

            with conn.cursor() as cur:

                cur.execute("INSERT INTO ativos (ticker, tipo, preco) values (%s, %s, %s)", (ticker, tipo, preco))

                conn.commit()

def excluir_ativo(id):

    print("\nGostaria de apagar:\n(1)Apagar um ativo\n(2)Apagar todos os ativos")
    
    apagar = int(input("\nEscolha uma opção acima: "))

    visualizar_ativos()

    if apagar == 1:

        print("\nGostaria de apagar qual id acima?")
            
        id = int(input("\nEscolha uma opção: "))

        with conectar_bd() as conn:

            with conn.cursor() as cur:

                cur.execute("DELETE FROM ativos WHERE id = %s",(id,))

                conn.commit()

        print("Ativo excluído com sucesso!")

    elif apagar == 2:

        print("\nGostaria de apagar toda a base de ativos?")

        confirmacao_exclusao = int(input("\n(1)Sim\n(2)Não\n"))

        if confirmacao_exclusao == 1:

            senha_exclusao = os.getenv('Senha_Exclusao')

            senha_secreta = str(input("\nDigite a senha para realizar essa Exclusão:"))

            if senha_exclusao == senha_secreta:
    
                with conectar_bd() as conn:
            
                    with conn.cursor() as cur:
            
                        cur.execute("DELETE FROM ativos")
            
                        conn.commit()

                print("Ativo excluído com sucesso!")

        elif confirmacao_exclusao == 2:

            print("\nRetornando ao inicio")