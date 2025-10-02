# Dada a lista ["banana", "uva", "maçã", "laranja"], ordene as palavras pelo último caractere.
lista = ["banana", "uva", "maçã", "laranja"]
ordenado = sorted(lista, key=lambda x : x[-1])
print(ordenado)