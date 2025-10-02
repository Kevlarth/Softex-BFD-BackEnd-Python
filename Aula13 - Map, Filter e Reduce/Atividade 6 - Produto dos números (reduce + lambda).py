from functools import reduce

# Usando reduce, calcule o produto (multiplicação) de todos os elementos da lista [2, 3, 4, 5].
lista: list[int] = [2, 3, 4, 5]
mult_sum: int = reduce(lambda x, y : x * y, lista)
print(mult_sum)