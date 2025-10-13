# 1 - Crie as classes Pessoa e Livro e demonstre uma relação de associação entre eles.

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.livro_favorito = None # A pessoa pode ou não ter um livro favorito

    def ler(self):
        if self.livro_favorito:
            print(f"{self.nome} está lendo '{self.livro_favorito.titulo}' de {self.livro_favorito.autor}.")
        else:
            print(f"{self.nome} não tem um livro favorito no momento.")


livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien")
pessoa1 = Pessoa("Ana")

pessoa1.livro_favorito = livro1

pessoa1.ler()

"""
A associação é o relacionamento mais geral entre duas classes. Nela, um objeto de uma classe se conecta ou "usa" um objeto de outra.
"""

# 2 - Crie as classes Aluno e Onibus. Crie um método em Aluno que use a classe Onibus.

class Onibus:
    def __init__(self, linha, capacidade):
        self.linha = linha
        self.capacidade = capacidade
        self.passageiros = 0

    def embarcar(self):
        if self.passageiros < self.capacidade:
            self.passageiros += 1
            print("Passageiro embarcou.")
            return True
        else:
            print("Ônibus lotado!")
            return False

class Aluno:
    def __init__(self, nome):
        self.nome = nome

    def pegar_onibus(self, onibus: Onibus):
        print(f"{self.nome} está tentando pegar o ônibus da linha {onibus.linha}.")
        onibus.embarcar()


onibus_circular = Onibus("Circular Campus", 50)
aluno_joao = Aluno("João")

aluno_joao.pegar_onibus(onibus_circular)
