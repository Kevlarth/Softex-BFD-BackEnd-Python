# Implemente um programa que abra um arquivo chamado dados.txt (não precisa existir).
# Use try e finally para garantir que uma mensagem de "Encerrando programa" seja sempre exibida.
from time import sleep

arquivo: str = "dados.txt"

try:
    print(f"Abrindo {arquivo} ")
    sleep(2)
    print(f"Arquivo {arquivo} aberto com sucesso")
    sleep(2)
    print(f"editando o conteúdo de {arquivo}")
    sleep(2)
    print(f"Salvando o conteúdo de {arquivo}")
    sleep(2)
    print(f"fechando {arquivo}")
    sleep(2)
except:
    print(f"Não é possível abrir {arquivo}.")
finally:
    print("Encerrando o programa.")