# Peça para o Aluno digitar um número.
# O programa deve dizer se ele é par ou ímpar
numero: int = int(input("Digite um número: "))
if (numero % 2 == 0):
    print(f"{numero} é par")
else:
    print(f"{numero} é ímpar")
