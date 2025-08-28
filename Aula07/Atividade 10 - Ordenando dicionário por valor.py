# Dado o dicionário:
pontuacoes: dict = {"João": 50, "Maria": 80, "Pedro": 70}
# Imprima os itens do dicionário ordenados pela pontuação (valor), do maior para o menor.

# Sort key
def value_getter(item):
     return item[1]

print(sorted(pontuacoes.items(), reverse=True, key=value_getter))