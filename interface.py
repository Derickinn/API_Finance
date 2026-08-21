import tkinter as tk
from tkinter import messagebox
from busca_ticker import buscar_ticker_fii, formula_cotacao_fii

janela = tk.Tk()

texto_inicio = tk.Label(janela, text="Digite o ticker do FII que deseja consultar:", font=("Arial", 14),)
texto_inicio.pack()

entrada = tk.Entry(janela)
entrada.pack()

def buscar():

    ticker = entrada.get()

    ticker, close_price, pvp, dividend_yield = formula_cotacao_fii(ticker)

    preco_recente = tk.Label(janela, text=f"Preço recente: {close_price}")
    preco_recente.pack()

    pvp_label = tk.Label(janela, text=f"P/Vp: {pvp['pvp']}")
    pvp_label.pack()

    dividend_yield_label = tk.Label(janela, text=f"Dividend Yield: {dividend_yield['dividend_yield_ttm']}%")
    dividend_yield_label.pack() 

botao_buscar = tk.Button(janela, text="Buscar", command=buscar)
botao_buscar.pack()

janela.geometry("600x700+650+100")

janela.mainloop()
