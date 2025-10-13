# 3 - Crie uma classe Funcionario e Departamento que contém uma lista de Funcionarios.
# Departamento deve agregar funcionários já criados.

class Funcionario:
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo

class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = [] # O departamento "tem" uma lista de funcionários

    def adicionar_funcionario(self, funcionario: Funcionario):
        print(f"Adicionando {funcionario.nome} ao departamento de {self.nome}.")
        self.funcionarios.append(funcionario)

    def listar_funcionarios(self):
        print(f"\nFuncionários do Departamento de {self.nome}:")
        for f in self.funcionarios:
            print(f"- {f.nome}, Cargo: {f.cargo}")


func1 = Funcionario("Carlos", "Desenvolvedor Sênior")
func2 = Funcionario("Mariana", "Gerente de Projetos")


dep_ti = Departamento("Tecnologia da Informação")

dep_ti.adicionar_funcionario(func1)
dep_ti.adicionar_funcionario(func2)

dep_ti.listar_funcionarios()


"""
A agregação é um tipo especial de associação onde uma classe é formada por outras classes.
"""

# 4 - Crie as classes Time e Jogador. Um Jogador tem nome e posição como atributos, enquanto Time agrega jogadores em uma lista.

class Jogador:
    def __init__(self, nome, posicao):
        self.nome = nome
        self.posicao = posicao

class Time:
    def __init__(self, nome):
        self.nome = nome
        self.jogadores = [] # O time "tem" uma lista de jogadores

    def contratar_jogador(self, jogador: Jogador):
        print(f"O time {self.nome} contratou {jogador.nome} ({jogador.posicao}).")
        self.jogadores.append(jogador)

    def mostrar_escalacao(self):
        print(f"\nEscalação do time {self.nome}:")
        if not self.jogadores:
            print("Nenhum jogador no time.")
        for j in self.jogadores:
            print(f"- {j.nome} ({j.posicao})")


j1 = Jogador("Neymar", "Atacante")
j2 = Jogador("Casemiro", "Meio-campista")

time_br = Time("Seleção Brasileira")

time_br.contratar_jogador(j1)
time_br.contratar_jogador(j2)

time_br.mostrar_escalacao()