# Dada a lista ["banana", "uva", "maçã", "laranja"], ordene as palavras pelo último caractere.
lista: list[str] = ["banana", "uva", "maçã", "laranja"]
ordenado: list[str] = sorted(lista, key=lambda x : x[-1])
print(ordenado)