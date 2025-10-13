# 5 - Crie a classe Carro que possui um Motor.
# O Motor deve ser criado dentro do Carro.
# Se o Carro deixar de existir, o Motor também deixa.
# Mostre isso criando e depois apagando o objeto.

class Motor:
    def __init__(self, potencia):
        print("Motor criado!")
        self.potencia = potencia

    def __del__(self):
        print("Motor destruído...")

class Carro:
    def __init__(self, modelo, potencia_motor):
        print(f"Criando o carro {modelo}...")
        self.motor = Motor(potencia_motor)
        self.modelo = modelo

    def __del__(self):
        print(f"Carro {self.modelo} está sendo destruído...")


print("Iniciando a criação do carro.")
meu_carro = Carro("Fusca", "1.6L")
print(f"Carro {meu_carro.modelo} com motor de potência {meu_carro.motor.potencia} existe.")

print("\nAgora, vamos apagar o objeto carro.")
del meu_carro 
print("\nFim do programa.")

"""
composição. É uma forma mais forte de agregação. A parte é criada dentro do todo e seu ciclo de vida está diretamente atrelado ao dele. 
"""

# 6 - Crie a classe Casa que é composta por vários Comodos (sala, cozinha, quarto, etc.). Cada Comodo deve ser criado dentro da Casa.

class Comodo:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
        print(f"Criado o cômodo: {self.tipo} ({self.nome})")

class Casa:
    def __init__(self, endereco):
        self.endereco = endereco
        self.comodos = []
        print(f"Construindo casa no endereço: {endereco}")
        self._construir_comodos()

    def _construir_comodos(self):
        self.adicionar_comodo("Principal", "Sala de Estar")
        self.adicionar_comodo("Gourmet", "Cozinha")
        self.adicionar_comodo("Suíte", "Quarto")
        self.adicionar_comodo("Social", "Banheiro")

    def adicionar_comodo(self, nome, tipo):
        novo_comodo = Comodo(nome, tipo)
        self.comodos.append(novo_comodo)

    def listar_comodos(self):
        print(f"\nCômodos da casa em {self.endereco}:")
        for c in self.comodos:
            print(f"- {c.tipo} ({c.nome})")


minha_casa = Casa("Rua dos Desenvolvedores, 101")
minha_casa.listar_comodos()

del minha_casa
