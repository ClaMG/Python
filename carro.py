class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def acelerar(self):
        print("Acalerando...")
class Carro(Veiculo):
    def abrir_portas(self):
        print("Abrindo portas...")

meu_carro = Carro(marca=input("Marca do carro: "), modelo = input("Modelo do carro: "))
meu_carro.acelerar()
meu_carro.abrir_portas()
    