class Calculadora:
    def somar(self, a, b):
        return a+b
    def somar(self, a, b, c):
        return a+b+c

calc = Calculadora()
print(calc.somar(2, 3, 0))
print(calc.somar(2, 3, 5))