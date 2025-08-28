# Crie um dicionário onde cada chave é o nome de um aluno e o valor é uma lista com 3 notas. Depois, imprima a média de cada aluno.
alunos: dict = {"Miguel": [8, 9, 8], "Isabella": [7, 8, 7], "Enrico": [6, 7, 6]}

for aluno in alunos:
    soma_notas: float = sum(alunos[aluno])
    quantidade_notas: float = len(alunos[aluno])
    print(f"A Média de {aluno} foi de {soma_notas/quantidade_notas:.2f}")