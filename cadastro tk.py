import tkinter as tk

janela=tk.Tk()
janela.title("cadastro")
janela.geometry("500x300")
janela.config(bg="pink")

nome = tk.Label(janela, text=" Informe seu nome: ",  bg="pink")
nome.pack()

entrada_nome = tk.Entry(janela)
entrada_nome.pack(pady=10, padx=10)

idade = tk.Label(janela, text=" Informe seu ano de nascimento: ",  bg="pink")
idade.pack()

entrada_idade = tk.Entry(janela)
entrada_idade.pack(pady=10, padx=10)

def calcular():
    n = (entrada_nome.get())
    a = int(entrada_idade.get())
    i = 2024 - a
    lb_infos.config(text= ('Ola ', n , ', Você tem ', i , ' anos')) #Arrumar(Fica aparecendo chaves no lugar das aspas)

button = tk.Button(janela, text="Enter", width=15, bg="lightblue", fg="navy", command=calcular)
button.pack()

lb_infos = tk.Label(janela, text="info", bg="pink")
lb_infos.pack(pady=10, padx=10)

janela.mainloop()