# Dada a lista ["uva", "banana", "maçã", "laranja"], ordene as palavras pelo tamanho usando sorted e lambda.
lista: list[str] = ["uva", "banana", "maçã", "laranja"]
ordenado: list[str] = sorted(lista, key=lambda x: len(x))
print(ordenado)