# 1 - Crie uma lista chamada livros contendo 3 livros diferentes e exiba a lista na tela.
livros: list[str] = ["Admirável Mundo Novo","Blade Runner", "O problema dos três corpos"]
print(livros)


# 2 - Usando a lista livros, exiba apenas o primeiro e o último elemento.
print(f"Primeiro elemento: {livros[0]}")
print(f"último elemento: {livros[-1]}")


# 3 - Adicione mais dois livros à lista livros usando o método append() e exiba a lista atualizada.
livros.append("Frankenstein")
livros.append("Neuromancer")
print(livros)


# 4 - Insira o livro "Duna" na segunda posição da lista livros usando insert().
livros.insert(1, "Duna")


# 5 - Remova o livro "Silêncio dos inocentes" da lista usando remove(). Se ele não existir, exiba a mensagem "Livro não encontrado".
if "Silêncio dos inocentes" in livros:
    livros.remove("Silêncio dos inocentes")
    print("Livro removido")
else:
    print("Livro não encontrado")


# 7 - Percorra a lista livros e exiba cada livro com a frase: "O livro <nome do livro> é interessante"
for livro in livros:
    print(f"O livro {livro} é interessante")
