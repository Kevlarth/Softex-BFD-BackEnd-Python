# Crie uma função sacar(saldo, valor) que:
# Lance (raise) uma exceção personalizada SaldoInsuficienteError se o valor for maior que o saldo.
# Caso contrário, retorne o novo saldo.
# Teste a função dentro de um try-except e exiba uma mensagem apropriada ao usuário.

class SaldoInsuficienteError(Exception): ...

def sacar(saldo: float, valor: float) -> float:
    if saldo < valor:
        raise SaldoInsuficienteError("Saldo insuficiente para saque.")
    return  saldo - valor
        

try:
    saldo_atual: float = 1000
    valor_saque: float = 250
    novo_saldo: float = sacar(saldo_atual, valor_saque)
    print(f"Operação de saque no valor de {valor_saque:.2f} efetivado.\nNovo saldo: {novo_saldo:.2f}")
except SaldoInsuficienteError as erro:
    print(f"{type(erro).__name__}: {erro}")

try:
    saldo_atual: float = 750
    valor_saque: float = 1000
    novo_saldo: float = sacar(saldo_atual, valor_saque)
    print(f"Operação de saque no valor de {valor_saque:.2f} efetivado.\nNovo saldo: {novo_saldo:.2f}")
except SaldoInsuficienteError as erro:
    print(f"{type(erro).__name__}: {erro}")