class ContaCorrente:
    def  _init_ (self, numero_conta, nome, saldo ):
        self.saldo  =  saldo
        self.numero_conta  =  numero_conta
        self.nome  =  nome
    
    def saldo_atual(self, deposito, saque, transferencia):
        if transferencia == 1:
            self.saldo  +=  deposito
            return  self.saldo
        else:
            self.saldo  -=  saque
            return  self.saldo
    def fim(self, saldo_atual,):
        nome =input('Digite seu nome: ')
        numero_conta= input("Digite o numero da sua conta: ")
        saldo = int(input("Digite seu saldo: ")) 
        trasferencia = int(input("tranferencia: "))
        if trasferencia == 1:
            deposito = int(input("Valor do seu deposito"))
        elif trasferencia == 2:
            saque = int(input("Valor do seu saque"))
        print("Seu nome é ", nome, ", Numero da sua conta é ", numero_conta, ", Seu saldo é de ", saldo_atual )
        

CC1 = ContaCorrente()
CC1.fim()