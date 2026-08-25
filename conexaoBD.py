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

            for ativo in ativos:

                print(ativo)