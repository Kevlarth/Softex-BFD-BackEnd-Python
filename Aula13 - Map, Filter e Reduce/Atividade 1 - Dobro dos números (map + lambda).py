# Dada a lista [1, 2, 3, 4, 5], use map com lambda para gerar uma nova lista com o dobro de cada número.
lista: list[int] = [1, 2, 3, 4, 5]
dobro: list[int] = list(map(lambda num : num * 2 , lista))
print(dobro)