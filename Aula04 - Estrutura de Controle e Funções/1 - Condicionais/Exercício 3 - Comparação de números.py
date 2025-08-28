# Pedir dois números ao usuário e mostrar qual o maior ou se são iguais.
primeiro_numero: float = float(input("Digite o primeiro número: "))
segundo_numero: float = float(input("Digite o segundo número: "))
if (primeiro_numero == segundo_numero):
    print("Os números são iguais")
elif (primeiro_numero > segundo_numero):
    print(f"O número {primeiro_numero}, foi digitado primeiro e é o maior!")
else:
    print(f"O número {segundo_numero}, foi digitado por último e é o maior!")
