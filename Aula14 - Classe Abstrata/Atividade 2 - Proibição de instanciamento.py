# Tente instanciar diretamente a classe Animal da questão anterior e explique o erro gerado pelo Python.

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def falar(self):
        ...


elefante: Animal = Animal()

"""
Traceback (most recent call last):
  File "/workspaces/Softex-BFD-BackEnd-Python/Aula14 - Classe Abstrata/Atividade 2 - Proibição de instanciamento.py", line 11, in <module>
    elefante: Animal = Animal()
                       ^^^^^^^^
TypeError: Can't instantiate abstract class Animal without an implementation for abstract method 'falar'
"""

""""
O erro `TypeError` acontece na tentativa de criar um objeto diretamente de uma classe abstrata (`Animal`), o que é proibido.
Isso ocorre porque a classe é um "modelo inacabado", servindo apenas como um contrato que obriga suas subclasses a implementar o método `falar`.
"""