# Crie uma função chamada calculadora que tenha dentro dela outras funções (somar, subtrair, multiplicar, dividir).
# A função principal deve permitir escolher a operação e retornar o resultado.

def calculadora(x: float, y: float) -> float | None:
    def somar(num1: float, num2: float) -> float:
        return num1 + num2
    
    def subtrair(num1: float, num2: float) -> float:
        return num1 - num2
    
    def multiplicar(num1: float, num2: float) -> float:
        return num1 * num2
    
    def dividir(num1: float, num2: float) -> float:
        if num2 == 0:
            print("Erro: Divisão por zero não é permitida.")
            return None
        return num1 / num2

    operacao: str = input("Digite qual a operação desejada: ")

    match operacao.lower():
        case "soma" | "somar" | "+":
            return somar(x,y)
        case "subtração" | "subtrair" | "-":
            return subtrair(x,y)
        case "multiplicação" | "multiplicar" | "*":
            return multiplicar(x,y)
        case "divisão" | "dividir" | "/":
            return dividir(x,y)
        case _:
            print("Operação inválida. Por favor, escolha 'soma', 'subtração', 'multiplicação' ou 'divisão'.")
            return None

resultado: float = calculadora(12,8)
print(resultado)