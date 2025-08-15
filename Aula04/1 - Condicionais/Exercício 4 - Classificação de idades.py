# Ler a idade e dizer:
# criança até 12 anos, Adolescente entre 13 e 17 anos, Adulto entre 18 e 64 anos e Idoso maior ou igual a 65 anos
idade: int = int(input("Digite a idade: "))
"""
Link -> https://encurtador.com.br/EO389
Algumas pesquisas indicam um limite natural de 120 a 150 anos, segundo a revista Nature Communications,
considerando a capacidade do corpo de se recuperar de danos e manter o equilíbrio. 
"""
if (idade > 0 or idade < 151):
    if (idade >= 65):
        print("Idoso")
    elif (idade >= 18 or idade < 65):
        print("Adulto")
    elif (idade >= 13 or idade < 18):
        print("Adolescente")
    else:
        print("Criança")
else:
    print("Idade Inválida")