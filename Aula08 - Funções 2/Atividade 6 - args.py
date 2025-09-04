# Crie uma função chamada media que receba uma quantidade variável de números e retorne a média deles. Teste com 3, 5 e 7 valores diferentes.

def media(*args: int) -> float:
    return sum(args)/len(args)

teste3 = media(5,4,9)
teste5 = media(8,35,27,2,51)
teste7 = media(84, 46, 74, 32, 9, 62, 15) 

print(
    f"Este é o resultado da media de 3 números: {teste3}\nEste é o resultado da media de 5 números: {teste5}\nEste é o resultado da media de 7 números: {teste7}"
    )