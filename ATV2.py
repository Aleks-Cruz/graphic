import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

janela = tk.Tk()
janela.title("Faz seu Cadastro ai seu Randola!!!!!!!!!!!! ")
janela.geometry("500x600")

ttk.Label(janela, text="Faça seu Cadastro", font=("Arial", 20, "bold")).pack()

entrada_nome = ttk.Entry(janela)
ttk.Label(janela, text="Nome").pack()
entrada_nome.pack()

entrada_sobrenome = ttk.Entry(janela)
ttk.Label(janela, text="Sobrenome").pack()
entrada_sobrenome.pack()

entrada_nascimento = ttk.Entry(janela)
ttk.Label(janela, text="Data de Nascimento").pack()
entrada_nascimento.pack()

entrada_cpf = ttk.Entry(janela)
ttk.Label(janela, text="CPF").pack()
entrada_cpf.pack()

entrada_cep = ttk.Entry(janela)
ttk.Label(janela, text="CEP").pack()
entrada_cep.pack()

entrada_sexo = ttk.Entry(janela)
ttk.Label(janela, text="Sexo").pack()
entrada_sexo.pack()

entrada_estado = ttk.Entry(janela)
ttk.Label(janela, text="Estado").pack()
entrada_estado.pack()

entrada_cidade = ttk.Entry(janela)
ttk.Label(janela, text="Cidade").pack()
entrada_cidade.pack()

entrada_senha = ttk.Entry(janela, show="*")
ttk.Label(janela, text="Senha").pack()
entrada_senha.pack()

mensagem = ttk.Label(janela, text="")
mensagem.pack(pady=10)

def fazer_login():
    dados = {
        "Nome": entrada_nome.get(),
        "Sobrenome": entrada_sobrenome.get(),
        "Data de Nascimento": entrada_nascimento.get(),
        "CPF": entrada_cpf.get(),
        "CEP": entrada_cep.get(),
        "Sexo": entrada_sexo.get(),
        "Estado": entrada_estado.get(),
        "Cidade": entrada_cidade.get(),
        "Senha": entrada_senha.get()
    }

    info = "\n".join(f"{chave}: {valor}" for chave, valor in dados.items())
    messagebox.showinfo("Dados do Usuário", info)

ttk.Button(janela, text="Enviar", command=fazer_login).pack(pady=10)

janela.mainloop()