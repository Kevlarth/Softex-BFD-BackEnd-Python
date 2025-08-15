# Ler números até o usuário digitar 0
# Mostrar a soma dos números digitados

"""
digitado: int = int(input("Digite um número: "))
total: int = 0
while (digitado != 0):
    total += digitado
    print(f"Total: {total}")
    digitado: int = int(input("Digite um número: "))
"""

total: int = 0
while True:
    digitado: int = int(input("Digite um número: "))
    if digitado == 0:
        break
    total += digitado
    print(f"Total: {total}")