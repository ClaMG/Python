import tkinter as tk

janela=tk.Tk()
janela.title("calculadora")
janela.geometry("500x300")
janela.config(bg="pink")

rotulo1 = tk.Label(janela, text=" Informe o primeiro número: ",  bg="pink")
rotulo1.pack()

entrada_num1 = tk.Entry(janela)
entrada_num1.pack(pady=10, padx=10)

rotulo2 = tk.Label(janela, text=" Informe o segundo número: ", bg="pink")
rotulo2.pack()

entrada_num2 = tk.Entry(janela)
entrada_num2.pack(pady=20, padx=20)

opcao = tk.IntVar()
rb_soma= tk.Radiobutton(janela, text="+", variable=opcao, value=1,  bg="pink")
rb_soma.pack()
rb_subtrai= tk.Radiobutton(janela, text="-", variable=opcao, value=2, bg="pink")
rb_subtrai.pack()
rb_multi= tk.Radiobutton(janela, text="*", variable=opcao, value=3, bg="pink")
rb_multi.pack()
rb_div= tk.Radiobutton(janela, text="/", variable=opcao, value=4, bg="pink")
rb_div.pack()

def calcular():
    num1 = float(entrada_num1.get())
    num2 = float(entrada_num2.get())
    operacao = opcao.get()
    if operacao ==1:
        resultado= num1+num2
    elif operacao ==2:
        resultado= num1-num2
    elif operacao ==3:
        resultado= num1*num2
    elif operacao ==4:
        if num2!=0:
            resultado= num1/num2
        else:
            resultado="dá certo não"
    else:
        resultado= "deu não"

    print(resultado)
    lb_resultado.config(text=resultado)

button = tk.Button(janela, text="Calcular", width=15, bg="lightblue", fg="navy", command=calcular)
button.pack()

lb_resultado = tk.Label(janela, text="resultado", bg="pink")
lb_resultado.pack(pady=10, padx=10)


janela.mainloop()