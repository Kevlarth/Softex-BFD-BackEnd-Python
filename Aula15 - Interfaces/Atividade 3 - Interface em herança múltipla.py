# Crie uma interface Imprimivel com o método imprimir().
# Crie outra interface Exportavel com o método exportar().
# Implemente uma classe Relatorio que herde de ambas e implemente os métodos.

from abc import ABC, abstractmethod

class IImprimivel(ABC):
    @abstractmethod
    def imprimir(self):
        ...

class IExportavel(ABC):
    @abstractmethod
    def exportar(self):
        pass

class Relatorio(IImprimivel, IExportavel):
    def imprimir(self):
        print(f"O relatório está sendo impresso...")

    def exportar(self):
        print(f"O relatório foi exportado com sucesso!")

trimestral: Relatorio = Relatorio()

trimestral.imprimir()
trimestral.exportar()