# Ler a nota de um aluno e mostrar:
# Aprovado se a nota for maior ou igual a 7.
# Recuperação se estiver entre 5 e 6.9
# Reprovado se for menor que 5.

nota: int = int(input("Digite a nota: "))
if (nota >= 0 and nota <=10):
    if (nota < 5):
        print("Reprovado")
    elif (nota < 7):
        print("Recuperação")
    else:
        print("Aprovado")
else:
    print("Nota inválida")