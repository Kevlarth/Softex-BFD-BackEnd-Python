# Crie um programa que receba dois números digitados pelo usuário com input().
# E mostre o resultado das quatro operações básicas.

print("====== Calculadora básica ======")
primeiro_numero = int(input("Digite o primeiro Número: "))
segundo_numero = int(input("Digite o segundo número: "))
print(f"\n===== Resultado =====\nSoma: {primeiro_numero+segundo_numero}\nSubtração: {primeiro_numero-segundo_numero}\nMultiplicação: {primeiro_numero*segundo_numero}\nDivisão: {primeiro_numero/segundo_numero}")