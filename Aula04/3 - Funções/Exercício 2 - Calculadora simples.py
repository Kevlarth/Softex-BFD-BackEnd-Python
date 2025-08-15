# Criar funções:
# somar(a, b)
# subtrair(a, b)
# multiplicar(a, b)
# dividir(a, b)
# Permitir que o usuário escolha a operação.

def calculadora_simples() -> None:

    def somar(x: float, y: float) -> float:
        return (x + y)

    def subtrair(x: float, y: float) -> float:
        return (x - y)

    def multiplicar(x: float, y: float) -> float:
        return (x * y)

    def dividir(x: float, y: float) -> float:
        return (x / y)

    a: float = float(input("Digite o primeiro número: "))
    operador: str = input("Digite a operação desejada (+, -, *, /): ")
    b: float = float(input("Digite o segundo número: "))

    if (operador == "+"):
        resultado: float = somar(a,b)
        print(resultado)
    
    elif (operador == "-"):
        resultado: float = subtrair(a,b)
        print(resultado)
    
    elif (operador == "*"):
        resultado:float = multiplicar(a,b)
        print(resultado)
    
    elif (operador == "/"):
        if b == 0:
            print("Operação inválida | Divisão por Zero")
        resultado = dividir(a,b)
        print(resultado)

    else:
        print("Operador inválido! Use +, -, * ou /")

calculadora_simples()