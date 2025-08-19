# 4) Crie uma nova lista só com números (inteiro e/ou ponto flutuante) e multiplique os
# elementos da lista por 5. O resultado deve ser uma nova lista com os elementos multiplicados.

lista_numerica = [1, 2, 3, 4, 5]
lista_multiplicada = []

for _ in range(len(lista_numerica)):
    lista_multiplicada.append(lista_numerica[_] * 5)
print(lista_multiplicada)