# Escreva uma função que recebe dois dicionários e retorna um novo dicionário contendo todos os pares chave-valor.
# Se houver chaves repetidas, o valor do segundo dicionário deve prevalecer.

def unir_dicionarios(x: dict, y: dict) -> dict:
    z: dict = x.copy()
    z.update(y)
    print(z)

dict1: dict = {'a': 1, 'b': 2, 'c': 3}
dict2: dict = {'b': 20, 'c': 30, 'd': 40}

unir_dicionarios(dict1, dict2)