# Crie uma função chamada dobro que recebe um número como parâmetro e retorna o dobro desse número. Teste chamando a função com diferentes valores.

def dobro(numero: int) -> int:
    return numero*2

numero = 12
for i in range(numero):
    dobrado = dobro(i)
    print(dobrado)