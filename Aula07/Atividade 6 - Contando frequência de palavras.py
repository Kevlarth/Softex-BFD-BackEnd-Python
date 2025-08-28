# Escreva uma função que receba uma lista de palavras e retorne um dicionário com a contagem de cada palavra.
palavras: list = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]

def contagem(elementos: list) -> dict:
    itens: dict = {}
    for elemento in elementos:
        if (elemento) in itens:
            itens[elemento] += 1
            continue
        itens[elemento] = 1
    print(itens)

contagem(palavras)