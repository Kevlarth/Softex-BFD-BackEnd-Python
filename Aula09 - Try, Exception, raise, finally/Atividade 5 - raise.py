# Crie uma função dividir(a, b) que lance (raise) uma exceção ZeroDivisionError se b for igual a zero.
# Caso contrário, retorne o resultado da divisão.

def dividir(a: int, b: int) -> float:
    if b == 0:
        raise ZeroDivisionError("Divisão por zero não é permitida.")
    return a / b

try:
    resultado = dividir(34, 0)
    print(f"Resultado: {resultado}")
except ZeroDivisionError as e:
    print(f"Erro: {e}")