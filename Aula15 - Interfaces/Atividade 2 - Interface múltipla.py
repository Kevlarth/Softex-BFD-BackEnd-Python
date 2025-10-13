# Crie duas interfaces: Ligavel (com o método ligar()) e Desligavel (com o método desligar()).
# Crie uma classe Computador que implemente ambas.
# Mostre seu uso.

from abc import ABC, abstractmethod

class ILigavel(ABC):
    @abstractmethod
    def ligar(self):
        ...

class IDesligavel(ABC):
    @abstractmethod
    def desligar(self):
        pass

class Computador(ILigavel, IDesligavel):
    def ligar(self):
        print("O computador está ligando ...\nO computador está ligado!")

    def desligar(self):
        print("O computador está desligando ...\nO computador está desligado!")

notebook: Computador = Computador()
notebook.ligar()
print()
notebook.desligar()


