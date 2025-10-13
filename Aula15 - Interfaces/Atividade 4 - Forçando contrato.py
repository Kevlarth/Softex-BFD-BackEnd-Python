# Crie uma interface Repositorio com os métodos salvar(objeto) e buscar(id).
# Depois, crie uma classe RepositorioMemoria que não implemente um dos métodos.
# O que acontece quando você tenta instanciá-la? Corrija o código.

from abc import ABC, abstractmethod

class IRepositorio(ABC):
    @abstractmethod
    def salvar(self, objeto: any):
        ...
    @abstractmethod
    def buscar(self, id: int):
        pass

class RepositorioMemoria(IRepositorio):
    ...

album: RepositorioMemoria = RepositorioMemoria() 

"""
Traceback (most recent call last):
  File "/workspaces/Softex-BFD-BackEnd-Python/Aula15 - Interfaces/Atividade 4 - Forçando contrato.py", line 18, in <module>
    album: RepositorioMemoria = RepositorioMemoria() 
                                ^^^^^^^^^^^^^^^^^^^^
TypeError: Can't instantiate abstract class RepositorioMemoria without an implementation for abstract methods 'buscar', 'salvar'
"""
