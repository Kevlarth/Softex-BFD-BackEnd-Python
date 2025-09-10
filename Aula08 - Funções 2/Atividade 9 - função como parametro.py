# Crie uma função chamada aplicar_operacao que receba dois números e uma função como parâmetros.
# A função deve aplicar a operação recebida (ex: soma, multiplicação). Exemplo:
# def soma(a, b): return a + b
# aplicar_operacao(3, 4, soma)

from typing import Callable

def somar(num1: float, num2: float) -> float:
    return num1 + num2
    
def subtrair(num1: float, num2: float) -> float:
    return num1 - num2
    
def multiplicar(num1: float, num2: float) -> float:
    return num1 * num2
    
def dividir(num1: float, num2: float) -> float | None:
    if num2 == 0:
        print("Erro: Divisão por zero não é permitida.")
        return None
    return num1 / num2
    
def aplicar_operacao(x: float, y: float, funcao: Callable[[float, float], float | None]):
    return funcao(x,y)


# --- Testando as operações ---
print(f"Soma: {aplicar_operacao(12, 8, somar)}")
print(f"Subtração: {aplicar_operacao(12, 8, subtrair)}")
print(f"Multiplicação: {aplicar_operacao(12, 8, multiplicar)}")
print(f"Divisão: {aplicar_operacao(12, 0, dividir)}") # Testando a divisão por zero
print(f"Divisão: {aplicar_operacao(12, 3, dividir)}")