# Crie uma função chamada mensagem que receba um nome como parâmetro e exiba a mensagem:

# "Olá, [nome]!"

# Caso o nome não seja informado, mostre "Olá, visitante!".

def mensagem(nome: str = "visitante") -> str:
    return print(f"Olá, {nome}!")

mensagem("Luiz")
mensagem()