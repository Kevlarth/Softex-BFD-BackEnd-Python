SELECT 
    nome AS nome_aluno,
    nota1,
    nota2,
    (nota1 + nota2)/2 AS media_notas
FROM aluno
WHERE media_notas >= 7
ORDER BY media_notas DESC
LIMIT 10;

SELECT COUNT(*) AS total_alunos
FROM aluno;

SELECT id_turma, COUNT(*) AS n_alunos
FROM aluno
GROUP BY id_turma
HAVING n_alunos > 20;