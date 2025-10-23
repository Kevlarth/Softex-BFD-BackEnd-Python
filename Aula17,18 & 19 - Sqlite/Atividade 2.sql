-- COUNT Mostre quantos alunos estão cadastrados na tabela Aluno. (Use a função COUNT)
SELECT COUNT(*) AS n_alunos_tabela FROM Aluno;

-- MIN Mostre a menor mensalidade entre todos os cursos cadastrados. (Use a função MIN)
SELECT MIN(mensalidade) AS menor_mensalidade
FROM Curso

-- MAX Mostre a maior nota1 registrada entre todos os alunos. (Use a função MAX)
SELECT MAX(nota1) AS maior_nota
FROM Aluno

-- SUM Calcule o valor total das mensalidades de todos os cursos. (Use a função SUM)
SELECT SUM(mensalidade) AS soma_mensalidades
FROM Curso

-- AVG Mostre a média geral da nota2 dos alunos. (Use a função AVG)
SELECT  AVG(nota2) as media_nota2
FROM Aluno