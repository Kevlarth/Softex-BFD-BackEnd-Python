# Dada a lista ["ana", "pedro", "maria"], use map e lambda para transformar em ["Ana", "Pedro", "Maria"].
lista: list[str] = ["ana", "pedro", "maria"]
alterado: list[str] = list(map(lambda x : x[0].upper() + x[1:], lista))
print(alterado)