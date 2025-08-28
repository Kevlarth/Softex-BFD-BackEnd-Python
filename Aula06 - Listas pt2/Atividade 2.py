# 6 - Crie uma lista chamada numeros com os valores [1, 2, 3, 2, 4, 2, 5]. Mostre quantas vezes o número 2 aparece na lista.
numeros: list[int] = [1, 2, 3, 2, 4, 2, 5]
print(numeros.count(2))


# 8 - Dada a lista idades = [12, 18, 25, 14, 30], use um laço para exibir somente as idades maiores ou iguais a 18.
idades = [12, 18, 25, 14, 30]
for idade in idades:
    if idade >= 18:
        print(idade)


# 9 - Crie uma lista valores = [10, 20, 30, 40]. Use um laço for para calcular manualmente a soma de todos os valores.
valores = [10, 20, 30, 40]
soma: int = 0
for valor in valores:
    soma += valor
print(soma)


# 10 - Use input para receber 3 notas de dois alunos. 
# As notas de cada aluno precisam ser armazenadas em uma lista separada que deve ser armazenada dentro de outra lista chamada notas,
# exemplo:  notas = [[7, 8, 9], [6, 5, 7]]
# No fim, imprima a média de cada aluno.

#Primeira tentativa
"""
notas_aluno: list[float] = [[] for x in range(2)]

for _ in range(3):
    nota1: float = float(input(f"Digite a { _ + 1 }ª nota do º aluno: "))
    notas_aluno[0].append(nota1)

for _ in range(3):
    nota2: float = float(input(f"Digite a { _ + 1 }ª nota do º aluno: "))
    notas_aluno[1].append(nota2)

media1: float = sum(notas_aluno[0]) / len(notas_aluno[0])
media2: float = sum(notas_aluno[1]) / len(notas_aluno[1])

print(media1)
print(media2)
"""

notas: list[list] = []
quantidade_alunos: int = 2
quantidade_notas: int = 3

for i in range(quantidade_alunos):
    alunos_notas: list = [
        float(input(f"Digite a {j+1}ª nota do {i+1}º Aluno: "))
        for j in range(quantidade_notas)
        ]
    notas.append(alunos_notas)

for i in range(quantidade_alunos):
    media: float = sum(notas[i]) / len(notas[i])
    print(f"A média do {i+1}º Aluno é {media}!")
