import sqlite3

try:
    db_connection = sqlite3.connect('Aula20 - SQLite & python/escola_v2.db')
except:
    print("Não foi possível conectar com o banco de dados, tente mais tarde!")

cursor = db_connection.cursor()

# 5 - Usando a query da questão 4, adicione um filtro para pegar apenas os alunos da turma 2 e imprima na tela.
cursor.execute("""
SELECT *
FROM 
    Aluno LEFT JOIN Turma 
WHERE Aluno.id_turma = Turma.id
AND Turma.id = 2   
""")

rows = cursor.fetchmany(5)

while rows:
    for row in rows:
        print(row)
    rows = cursor.fetchmany(5)
db_connection.close()