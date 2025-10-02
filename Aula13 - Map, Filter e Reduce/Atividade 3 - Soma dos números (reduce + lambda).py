from functools import reduce

# Usando reduce, some todos os números da lista [1, 2, 3, 4, 5].
lista = [1, 2, 3, 4, 5]
somados = reduce(lambda x, y : x + y, lista)
print(somados)