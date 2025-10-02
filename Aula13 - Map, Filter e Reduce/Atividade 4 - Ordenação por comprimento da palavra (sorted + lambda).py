# Dada a lista ["uva", "banana", "maçã", "laranja"], ordene as palavras pelo tamanho usando sorted e lambda.
lista = ["uva", "banana", "maçã", "laranja"]
ordenado = sorted(lista, key=lambda x: len(x))
print(ordenado)