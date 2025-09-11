# Crie uma exceção personalizada chamada IdadeInvalidaError.
# Depois, crie uma função cadastrar_idade(idade) que lance essa exceção caso a idade seja negativa.

class IdadeInvalidaError(Exception): ...

def cadastrar_idade(idade: int) -> int:
    if idade < 0:
        raise IdadeInvalidaError("Idade tem que ser maior que Zero")
    return idade

try:
    cadastrar_idade(-2)
except IdadeInvalidaError as erro:
    print(f"Erro: {erro}")