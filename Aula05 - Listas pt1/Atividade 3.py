# 5) Use o slice para criar uma nova lista que inclua apenas os elementos com índice 3 e 4 da lista a seguir:
# [ 1,2,3,4,5,6 ]
# Resultado esperado: [4,5]

lista_original: list[int] =  [ 1,2,3,4,5,6 ]
lista_partida: list[int] = lista_original[3:5]
print(lista_partida)