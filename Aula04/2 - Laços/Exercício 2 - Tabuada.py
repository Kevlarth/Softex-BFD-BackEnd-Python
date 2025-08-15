# Pedir um número para o usuário e imprimir a tabuada desse número de 1 a 10.
numero: int = int(input("Digite um número: "))
print(f"\n=== Tabuada do número {numero} ===")
for _ in range(1, 11):
    print(f"        {numero} * {_} = {numero * _}")
print("============================\n")