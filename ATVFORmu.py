import tkinter as tk
from tkinter import ttk
from tkinter import *

janela = tk.Tk()
janela.title("cadastro")

ttk.Label(janela,text="Dados pessoais").pack()

ttk.Label(janela,text="Nome").pack()
nome = ttk.Entry(janela)
nome.pack()

ttk.Label(janela,text="Idade").pack()
idade = ttk.Entry(janela)
idade.pack()

ttk.Label(janela,text="Dados profissionais").pack()

ttk.Label(janela,text="Escolaridade").pack()
esc = ttk.Combobox(janela,values=["Fundamental","Medio","Superior"])
esc.pack()

ttk.Label(janela,text="Area de Atuacao").pack()

area = tk.StringVar()

ttk.Radiobutton(janela,text="TI",variable=area,value="TI").pack()
ttk.Radiobutton(janela,text="ADM",variable=area,value="ADM").pack()
ttk.Radiobutton(janela,text="Saude",variable=area,value="Saude").pack()

def clicar():
    n = nome.get()
    i = idade.get()
    e = esc.get()
    a = area.get()

    msg = f"Nome: {n}\nIdade: {i}\nEscolaridade: {e}\nArea: {a}"


botao = ttk.Button(janela,text="enviar",command=clicar)
botao.pack()

janela.mainloop()