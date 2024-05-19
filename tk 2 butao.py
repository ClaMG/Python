import tkinter as tk

janela = tk.Tk()
janela.title("Sla")
janela.geometry("800x600")

def clique1():
    rotulo.config( text='você clicou no botão 1')

def clique2():
    rotulo.config( text='você clicou no botão 2')

rotulo = tk.Label(janela, text='Interface')
rotulo.pack(padx=15, pady=15)



botao = tk.Button(janela, text='Botão 1', bg='blue', command=clique1, height=50, width=35, relief='solid')
botao.pack(side='left', padx=15, pady=15)

botao2 = tk.Button(janela, text='Botão 2', bg='red', command=clique2, height=50, width=35, relief='solid')
botao2.pack(side='right',  padx=15, pady=15)

janela.mainloop()