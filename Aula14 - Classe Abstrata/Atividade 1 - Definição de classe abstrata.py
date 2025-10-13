# Crie uma classe abstrata chamada Animal que possua um método abstrato falar().
# Em seguida, crie duas classes concretas (Cachorro e Gato) que implementem esse método.
# Mostre o uso criando objetos e chamando o método falar().

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def falar(self):
        ...
    
class Cachorro(Animal):
    def falar(self):
        print("Au au au!")

class Gato(Animal):
    def falar(self):
        print("Miaaaauuu!")

dalila: Cachorro = Cachorro()
dalila.falar()

tico: Gato = Gato()
tico.falar()

