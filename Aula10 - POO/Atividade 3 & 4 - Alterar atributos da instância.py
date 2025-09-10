# Crie uma classe Carro com os atributos marca, modelo e ano.
# Use o método __init__ para inicializar esses valores. Crie três objetos e mostre suas informações.

class Carro:
    def __init__(self, marca: str, modelo: str, ano: int) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def __str__(self) -> str:
        return f"Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}"

carro1 = Carro("Toyota", "Corolla", 2020)
carro2 = Carro("Ford", "Fiesta", 2018)
carro3 = Carro("Chevrolet", "Onix", 2023)

print(carro1)
print()
print(carro2)
print()
print(carro3)

# Usando a classe Carro, crie um objeto e depois altere o valor de um de seus atributos (por exemplo, mudar o ano).
# Imprima antes e depois da alteração.

carro = Carro("Ford", "Mustang", 1965)
print(f"\n{carro}\n")
carro.marca, carro.modelo, carro.ano = "Tesla", "Model S", 2023
print(f"\n{carro}")