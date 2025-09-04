# Crie uma função chamada operacoes que receba dois números e retorne a soma, a subtração e a multiplicação deles.

def opercoes(num1: int, num2: int) -> int:
    return (num1+num2, num1-num2, num1*num2)

somado, subtraido, multiplicado = opercoes(12, 8)

print(f"A soma é: {somado}\nA Subtração é: {subtraido}\nA multiplicação é: {multiplicado}")