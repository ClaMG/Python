class ContaCorrente:
    def _init_(self, numero_conta, nome_correntista, saldo):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente para efetuar o saque.")

# Exemplo de uso:
minha_conta = ContaCorrente("123456", "Fulano", 1000.0)
print("Saldo inicial:", minha_conta.saldo)

minha_conta.deposito(500.0)
print("Saldo após depósito:", minha_conta.saldo)

minha_conta.saque(200.0)
print("Saldo após saque:", minha_conta.saldo)

minha_conta.saque(1500.0)  # Tentativa de saque com saldo insuficiente