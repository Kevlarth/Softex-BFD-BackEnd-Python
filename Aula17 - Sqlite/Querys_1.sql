SELECT nome, (nota1 + nota2)/2 AS media
FROM aluno
WHERE (nota1 + nota2)/2 >= 7
ORDER BY media DESC
LIMIT 10;

SELECT COUNT(*) AS total_alunos
FROM aluno;

SELECT id_turma, COUNT(*) AS total_alunos
FROM aluno
GROUP BY id_turma;