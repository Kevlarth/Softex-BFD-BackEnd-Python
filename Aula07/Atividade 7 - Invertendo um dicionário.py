# Dado o dicionário:
d: dict = {"a": 1, "b": 2, "c": 3}
# Crie um novo dicionário invertendo as chaves e os valores: {1: "a", 2: "b", 3: "c"}.

w: dict = {}

for item in d:
    w[d[item]] = item
print(w)
