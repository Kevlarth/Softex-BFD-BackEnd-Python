# Crie um programa que peça ao usuário um número inteiro e verifique se ele é par.
# Use:
# try para a conversão,
# else para verificar se é par ou ímpar,
# finally para exibir "Fim do programa".

try:
    ehpar: int = int(input("Digite um número para verificarmos se é par: "))
except:
   print("Utilize apenas números.") 
else:
    if ehpar % 2 != 0:
        print(f"O número {ehpar} não é par.")
    if ehpar % 2 == 0:
        print(f"O número {ehpar} é par.")
finally:
    print("Fim do programa.")