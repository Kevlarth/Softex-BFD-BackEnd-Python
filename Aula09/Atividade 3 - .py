# Crie um programa que peça ao usuário um número inteiro. Se a conversão for bem-sucedida, mostre uma mensagem usando o bloco else.

try:
    inteiro: int = (int(input("Digite um número inteiro: ")))
except:
    print("Tipo diferente de inteiro")
else:
    print(f"Você digitou o número {inteiro}.")