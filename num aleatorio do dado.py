import random
class dado:
    def __init__(self, numero_lados):
        self.numero_lados = numero_lados
    def lancar_dados(self):
        return random.randint(1,self.numero_lados)

d4 = dado(4)        
d6 = dado(6)        
d8 = dado(8)        
d10 = dado(10)        
d12 = dado(12)        
d20 = dado(20) 

print("O resultado do lançamento do d4 é", d4.lancar_dados())
print("O resultado do lançamento do d6 é", d6.lancar_dados())
print("O resultado do lançamento do d8 é", d8.lancar_dados())
print("O resultado do lançamento do d10 é", d10.lancar_dados())
print("O resultado do lançamento do d12 é", d12.lancar_dados())
print("O resultado do lançamento do d20 é", d20.lancar_dados())