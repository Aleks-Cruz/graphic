import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

janela = tk.Tk()
janela.title("Login do Rei delas")
janela.geometry("500x500")

ttk.Label(janela, text="Login do REI", font=("Arial", 20, "bold")).pack()

ttk.Label(janela, text="Usuário").pack()
entrada_usuario = ttk.Entry(janela)
entrada_usuario.pack()

ttk.Label(janela, text="Senha").pack()
entrada_senha = ttk.Entry(janela, show="*")
entrada_senha.pack()

mensagem = ttk.Label(janela, text="")
mensagem.pack()

def fazer_login():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()

    mensagem.config(text="USUÁRIO LOGADO COM SUCESSO")


    
    imagem = tk.PhotoImage(file="Cadeira.png")
    tk.Label(janela, image=imagem).grid(row=3,column=4)

ttk.Button(janela, text="Enviar", command=fazer_login).pack()

janela.mainloop()