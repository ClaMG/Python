class pessoa:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email
    def saudacao(self):
        print("Bem vindx", self.nome, "\nSua idade:", self.idade, "\nSeu e-mail:", self.email)
        
humano = pessoa(nome= input("Qual seu nome: "), idade=int(input("Qual sua idade: ")), email=input("Qual seu email: "))
humano.saudacao()