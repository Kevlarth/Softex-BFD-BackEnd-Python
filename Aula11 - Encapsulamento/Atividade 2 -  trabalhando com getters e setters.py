# Crie uma classe, Pessoa, que tenha os atributos: nome, data de nascimento, cpf, identidade.
# Deixe os atributos cpf e identidade como privado e monte os métodos setters e getters para acessar e editar os valores

class Pessoa:
    def __init__(self, nome: str, data_nascimento: str, cpf: str, identidade: str):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.__cpf = cpf
        self.__identidade = identidade

    def get_cpf(self) -> str:
        return self.__cpf
    
    def get_identidade(self) -> str:
        return self.__identidade
    
    def set_cpf(self, cpf: str) -> None:
        self.__cpf = cpf

    def set_identidade(self, identidade: str) -> None:
        self.__identidade = identidade