import math

class circulo: 
    def __init__(self, raio):
        self.raio = raio
    def calcular_a(self):
        return (math.pi* self.raio)
    def calcular_p(self):
        return(2 * math.pi * self.raio)
cir = circulo(raio = float(input("Valor do raio: ")))
print("Area do circulo: ", cir.calcular_a())    
print("Perímetro do circulo: ", cir.calcular_p())