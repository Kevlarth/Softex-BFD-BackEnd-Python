# Peça ao usuário dois números e tente multiplicá-los.
# Se o usuário digitar algo inválido, exiba uma mensagem de erro.

try:
    numero1: float = float(input("Digite o primeiro número: "))
    numero2: float = float(input("Digite o segundo número: "))
    print(numero1*numero2)
except:
    print("Error: Digite apenas números")