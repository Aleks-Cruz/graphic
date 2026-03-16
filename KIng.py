import tkinter as tk

janela_main = tk.Tk()

janela_main.title("My king")
janela_main.configure(background="yellow")
janela_main.minsize(200,200)
janela_main.maxsize(500,500)
janela_main.geometry("300x300")


tk.Label(
    janela_main,
    text="Seja Bem vindo meu REI",
    bg="black",
    fg="white",
    font=("Arial",20)
).pack()

tk.Label(
    janela_main,
    text="Coroa do meu REI",
    bg="orange",
    font=("Arial",20)
).pack()


imagem = tk.PhotoImage(file="REI.png") 
tk.Label(janela_main, image=imagem).pack()

janela_main.mainloop()