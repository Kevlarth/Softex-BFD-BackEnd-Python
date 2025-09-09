# Modifique a classe ContaBancaria para que o método sacar retorne True se a operação for bem-sucedida e False caso contrário.
# Teste o retorno e imprima mensagens adequadas.

class ContaBancaria:
    def __init__(self, titular: str, saldo: float = 0):
        self.titular = titular
        self.saldo = saldo

    def __str__(self):
        return f"Conta corrente do Titular {self.titular}, possui saldo de: {self.saldo:.2f}"

    def depositar(self, valor: float):
        self.saldo += valor
        return f"Operação de depósito no valor de {valor:.2f} efetivado."

    def sacar(self, valor: float):
        if self.saldo >= valor:
            self.saldo -= valor
            return (f"Operação de saque no valor de {valor:.2f} efetivado.", True)
        else:
            return (f"Saldo insuficiente para a operação.", False)

contaBB: ContaBancaria = ContaBancaria("Marivaldo", 500.00)
print(contaBB)
print(contaBB.depositar(250.00))
print(contaBB)
print(contaBB.sacar(150.00))
print(contaBB)
print(contaBB.sacar(700.00))


