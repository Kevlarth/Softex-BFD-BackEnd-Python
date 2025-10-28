import sqlite3

try:
    db_connection = sqlite3.connect('Aula20 - SQLite & python/escola_v2.db')
except:
    print("Não foi possível conectar com o banco de dados, tente mais tarde!")

cursor = db_connection.cursor()

# 4 - Use Left Join com as tabelas Aluno e Turma e imprima todos os dados da tabela.
cursor.execute("""
SELECT *
FROM 
    Aluno LEFT JOIN Turma 
WHERE Aluno.id_turma == Turma.id   
""")

rows = cursor.fetchmany(5)

while rows:
    for row in rows:
        print(row)
    rows = cursor.fetchmany(5)
db_connection.close()