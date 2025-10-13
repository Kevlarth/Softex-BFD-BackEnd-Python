# Defina uma classe abstrata FormaGeometrica com dois métodos abstratos: area() e perimetro().
# Crie uma classe concreta Retangulo que herde de FormaGeometrica e implemente os dois métodos.
# Teste criando um objeto e calculando sua área e perímetro.

from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    @abstractmethod
    def area(self):
        ...
    @abstractmethod
    def perimetro(self):
        ...

class Retangulo(FormaGeometrica):
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def area(self):
        print(f"A área do retângulo é medido multiplicando a base por sua altura.\nA área deste retângulo é: {self.base * self.altura}")

    def perimetro(self):
        print(f"O perímetro de um retângulo é a soma de todos os seus quatro lados.\nO perímetro deste retângulo é: {(self.base * self.altura) * 2}")

retangulo: Retangulo = Retangulo(3, 4)
retangulo.area()
retangulo.perimetro()


