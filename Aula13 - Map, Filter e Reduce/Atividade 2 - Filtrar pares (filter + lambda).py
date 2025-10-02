# Dada a lista [10, 15, 20, 25, 30], use filter com lambda para obter apenas os números pares.
lista: list[int] = [10, 15, 20, 25, 30]
pares: list[int] = list(filter(lambda num : num % 2 == 0, lista))
print(pares)

