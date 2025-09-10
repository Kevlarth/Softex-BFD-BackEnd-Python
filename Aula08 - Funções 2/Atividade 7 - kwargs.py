# Crie uma função chamada dados_pessoais que receba informações de uma pessoa (nome, idade, cidade, etc.) 
# usando **kwargs e imprima cada dado em uma linha. Exemplo de chamada:
# dados_pessoais(nome="Ana", idade=25, cidade="Recife")
from typing import Any

def dados_pessoais(**kwargs: dict[Any, Any]) -> str:
    for key, value in kwargs.items():
        print(f"{key}: {value}")

dados_pessoais(nome="Ana", idade=25, cidade="Recife")