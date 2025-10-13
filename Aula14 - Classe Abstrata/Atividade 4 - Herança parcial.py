# Crie uma classe abstrata Transporte com dois métodos abstratos: mover() e parar().
# Depois, crie uma subclasse Carro que implemente apenas o método mover().
# O que acontece quando você tenta instanciar Carro? Corrija implementando o segundo método.

from abc import ABC, abstractmethod

class Transporte(ABC):
    @abstractmethod
    def mover(self):
        ...

    @abstractmethod
    def parar(self):
        ...

class Carro(Transporte):
    def mover(self):
        print(f"O carro está se movendo!")

    def parar(self):
        print(f"O carro está parando...\nO carro está parado!")


camaro: Carro = Carro()
camaro.mover()
camaro.parar()

# Antes da implementação do método parar
"""
Traceback (most recent call last):
  File "/workspaces/Softex-BFD-BackEnd-Python/Aula14 - Classe Abstrata/Atividade 4 - Herança parcial.py", line 21, in <module>
    camaro: Carro = Carro()
                    ^^^^^^^
TypeError: Can't instantiate abstract class Carro without an implementation for abstract method 'parar'
"""