# Escreva um programa que peça ao usuário para digitar um número.
# Trate o erro caso ele digite algo que não seja um número inteiro.

try:
    numero: int = int(input("Digite um número inteiro: "))
except:
    print("Error: Use apenas números inteiros")