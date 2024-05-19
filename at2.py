class ContaCorrente:

    def _init_(self,numero_conta, nome_correntista,saldo=0):
        self.saldo = saldo
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista

    def deposito(self,valor_deposito):
        self.saldo += valor_deposito
        return self.saldo

    def saque(self,valor_saque):
        self.saldo -= valor_saque
        return self.saldo

CC1 = ContaCorrente(250,'Yann Schmitt')

print (CC1._dict_)

CC1.deposito(25)
print (CC1._dict_)

CC1.saque(10)
print (CC1._dict_)