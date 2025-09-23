# Na classe, ContaBancaria, converta saldo para uma atributo privado.
# Crie um método setter e um getter para acessar e modificar essa atributo, seguindo uma regra lógica (Ex: saldo não pode ser negativo)

class ContaBancaria:
    def __init__(self, titular: str, saldo: float = 0) -> None:
        self.titular = titular
        self.__saldo = saldo

    def __str__(self) -> str:
        return f"Conta corrente do Titular {self.titular}, possui saldo de: {self.saldo:.2f}"

    def depositar(self, valor: float) -> str:
        self.__saldo += valor
        return f"Operação de depósito no valor de {valor:.2f} efetivado."

    def sacar(self, valor: float) -> tuple[str, bool]:
        if self.__saldo >= valor:
            self.__saldo -= valor
            return (f"Operação de saque no valor de {valor:.2f} efetivado.", True)
        else:
            return (f"Saldo insuficiente para a operação.", False)
        
       # Getters
    def get_saldo(self):
        return self.__saldo
    
    # Setters
    def set_saldo(self, valor):
        if valor < 0:
            print("Saldo não pode ser negativo")
        else:
            self.__saldo = valor


contaBB: ContaBancaria = ContaBancaria("Marivaldo", 500.00)
print(contaBB)
print(contaBB.depositar(250.00))
print(contaBB)
print(contaBB.sacar(150.00))
print(contaBB)
print(contaBB.sacar(700.00))