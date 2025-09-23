# 6 - Crie uma classe Autenticacao com um método login().
# Crie outra classe Permissao com um método verificar_permissao().
# Em seguida, crie uma classe Administrador que herda de ambas. Como usar os métodos herdados?

# 7 - Usando o exemplo anterior, adicione um método status() em Autenticacao e também em Permissao.
# Se a classe Administrador herda das duas, qual versão de status() será chamada?
# Use Administrador.__mro__ para mostrar a ordem.

class Autenticacao:
    def login(self) -> str:
        return f"Realizando o Login na plataforma ..."
    
    def status(self) -> str:
        return f"Autenticação Válidada"

class Permissao:
    def verificar_permissao(self) -> str:
        return f"Verificando a permissão na plataforma ..."
    
    def status(self) -> str:
        return f"Permissão concedida"

class Administrador(Autenticacao, Permissao):
    ...

admin = Administrador()

print(admin.login())
print(admin.verificar_permissao())
print(Administrador.__mro__)

# mro legível
def formatar_mro(classe):
    """
    Retorna uma string formatada da Ordem de Resolução de Métodos (MRO)
    de uma classe, excluindo a classe 'object'.
    """
    mro_tuple = classe.__mro__
    mro_filtered = [cls.__name__ for cls in mro_tuple[:-1]]
    return ' -> '.join(mro_filtered)

print(f"MRO de Administrador: {formatar_mro(Administrador)}")