# 1) Crie uma lista que contenha diferentes tipos de dados (string, inteiro, outra lista…)
from typing import Any

listagem: list[Any] = ["teste", 1, ["..."]]

# 2) Usando a lista criada na questão anterior, use o método insert ou append para 
# adicionar mais dois elementos a lista e use remove, pop ou del para remover um 
# elemento da lista.

print(listagem)
listagem.insert(2,12.80)
listagem.append("último")
print(listagem)
listagem.remove(1)
listagem.pop()
del listagem[0]
print(listagem)

# 3) Faça uma cópia da lista da questão anterior. Use a função id para verificar se
# realmente criou uma lista nova (obs: mesmo valor de ID indica que é o mesma lista
# e não uma nova)

nova_listagem = listagem.copy()

print(id(listagem))
print(id(nova_listagem))