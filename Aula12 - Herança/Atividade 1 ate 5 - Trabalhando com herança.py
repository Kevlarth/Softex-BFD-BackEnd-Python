# 1 - Crie uma classe Usuario com atributos nome e email.
# Depois, crie uma classe Cliente que herde de Usuario.
# Crie uma instancia de um cliente e acesse todos os atributos.

# 2 - Implemente um método exibir_informacoes() na classe Usuario e herde esse método em Cliente.
# Mostre como chamar o método herdado a partir de um objeto Cliente.

# 3 - Na classe Usuario, crie um método saudacao() que retorna "Olá, usuário".
# Na classe Cliente, sobrescreva esse método para retornar "Olá, cliente".
# Mostre como funciona a chamada. 

# 4 - Na classe Cliente, adicione o atributo saldo.
# Adicione um método construtor em Cliente que inicialize também os atributos de Usuario usando super().

# 5 -  Crie uma classe Funcionario que herda de Usuario e, em seguida, crie uma classe Gerente que herda de Funcionario.
# Mostre como instanciar um gerente e acessar seus atributos.


from decimal import Decimal

class Usuario:
    def __init__(self, nome: str, email: str) -> None:
        self.nome = nome
        self.email = email

    def __repr__(self) -> str:
        return f"Usuario(nome='{self.nome}', email='{self.email}')"

    def exibir_informacoes(self) -> None:
        return print(f"Exibindo informações de {self.nome} - ({self.email})")

    def saudacao(self) -> str:
        return f"Olá, Usuário"
    
class Cliente(Usuario):
    def __init__(self, nome: str, email: str, saldo: Decimal) -> None:
        super().__init__(nome, email)
        self.saldo = saldo

    def __repr__(self) -> str:
        # Pega a representação do pai e adiciona o novo atributo
        usuario_repr = super().__repr__().replace("Usuario", "Cliente")
        return f"{usuario_repr.removesuffix(')')}, saldo={self.saldo})"

    def saudacao(self) -> str:
        return f"Olá, Cliente"

class Funcionario(Usuario):
    ...

class Gerente(Funcionario):
    def __repr__(self) -> str:
        gerente_repr = super().__repr__().replace("Usuario", "Gerente")
        return f"{gerente_repr}"


cliente = Cliente("Zezo", "zezo@gmail.com", 200)
print(cliente)
cliente.exibir_informacoes()
print(f" Exibindo método sobrescrito: {cliente.saudacao()}")
gerente = Gerente("Roberval", "Roberval@gmail.com")
print(gerente)