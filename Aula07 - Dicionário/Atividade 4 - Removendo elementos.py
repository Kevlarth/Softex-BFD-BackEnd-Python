# Dado o dicionário:
carro: int = {"marca": "Ford", "modelo": "Fiesta", "ano": 2010}
# Remova a chave "ano" do dicionário.
del carro["ano"] # ou carro.pop("ano")
print(carro)