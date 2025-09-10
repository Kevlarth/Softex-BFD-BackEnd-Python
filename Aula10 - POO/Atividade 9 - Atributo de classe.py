# Crie uma classe Cachorro com um atributo de classe especie = "Canis familiaris" e atributos de instância nome e idade.
# Mostre a diferença entre acessar especie pelo objeto e pela classe.

class Cachorro:
    especie: str = "Canis familiaris"
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

doguito: Cachorro = Cachorro("Pérola", 1)

print(f"Acessando pela classe Cachoro.especie: {Cachorro.especie}")
print(f"Acessando pela Instância: {doguito.especie}")