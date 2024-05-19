class calculadora:
    def __init__(self):
        pass
    def soma(self, num1, num2):
        return num1+num2
    def subtracao(self, num1, num2):
        return num1-num2
    def multiplicacao(self, num1, num2):
        return num1*num2
    def divisao(self, num1, num2):
       if num2 != 0:
            return num1/num2
       else:
           return("Pode não")
    def calcular (self):
        operacao = input('Informe a operação (+,-,*,/): ')
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        if operacao == "+":
            minhac= calculadora()
            resultado1= minhac.soma(num1, num2)
            print("Soma:", resultado1)
        elif operacao == "-":
            minhac= calculadora()
            resultado2= minhac.subtracao(num1, num2)
            print("Subtração:", resultado2)
        elif operacao == "*":
            minhac= calculadora()
            resultado3= minhac.multiplicacao(num1, num2)
            print("Mutiplicação:", resultado3)
        elif operacao == "/":
            minhac= calculadora()
            resultado4= minhac.divisao(num1, num2)
            print("Divisão:", resultado4)

resultadocalc = calculadora()
resultadocalc.calcular()