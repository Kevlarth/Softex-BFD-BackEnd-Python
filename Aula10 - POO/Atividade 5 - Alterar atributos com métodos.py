# Crie uma classe ContaBancaria com os atributos titular e saldo.
# Adicione um método depositar(valor) que aumenta o saldo e um método sacar(valor) que diminui o saldo (se houver saldo suficiente).
# Teste com depósitos e saques.

class ContaBancaria:
    def __init__(self, titular: str, saldo: float = 0) -> None:
        self.titular = titular
        self.saldo = saldo

    def __str__(self) -> str:
        return f"Conta corrente do Titular {self.titular}, possui saldo de: {self.saldo:.2f}"

    def depositar(self, valor: float) -> str:
        self.saldo += valor
        return f"Operação de depósito no valor de {valor:.2f} efetivado."

    def sacar(self, valor: float) -> str:
        if self.saldo >= valor:
            self.saldo -= valor
            return f"Operação de saque no valor de {valor:.2f} efetivado."
        else:
            return f"Saldo insuficiente para a operação."

contaBB: ContaBancaria = ContaBancaria("Marivaldo", 500.00)
print(contaBB)
print(contaBB.depositar(250.00))
print(contaBB)
print(contaBB.sacar(150.00))
print(contaBB)