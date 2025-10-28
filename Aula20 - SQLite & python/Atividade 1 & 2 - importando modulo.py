# 1 - Importe o módulo sqlite3 e faça a conexão com o banco de dados escola_v2.db
import sqlite3

try:
    db_connection = sqlite3.connect('Aula20 - SQLite & python/escola_v2.db')
except:
    print("Não foi possível conectar com o banco de dados, tente mais tarde!")

# 2 - Faça a query para pegar toda a tabela alunos e imprima na tela.

cursor = db_connection.cursor()

cursor.execute("""
SELECT * FROM 'Aluno'
""")

rows = cursor.fetchmany(5)

while rows:
    for row in rows:
        print(row)
    rows = cursor.fetchmany(5)
db_connection.close()






