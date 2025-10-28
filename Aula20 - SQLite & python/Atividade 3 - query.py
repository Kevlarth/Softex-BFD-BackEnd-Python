import sqlite3

try:
    db_connection = sqlite3.connect('Aula20 - SQLite & python/escola_v2.db')
except:
    print("Não foi possível conectar com o banco de dados, tente mais tarde!")

cursor = db_connection.cursor()

# 3 - Obtenha a media entre nota1 e nota2 dos alunos, ordene em ordem decrescente e retorne apenas os 10 maiores notas.
# No fim imprima na tela a lista desses alunos e suas médias.

cursor.execute("""
SELECT 
    nome, 
    (nota1 + nota2)/2 AS media_notas
FROM 
    Aluno
ORDER BY 
    media_notas DESC
LIMIT 10
    
""")

rows = cursor.fetchmany(5)

while rows:
    for row in rows:
        print(row)
    rows = cursor.fetchmany(5)
db_connection.close()