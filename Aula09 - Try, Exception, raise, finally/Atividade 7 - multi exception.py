# Peça ao usuário dois números e divida o primeiro pelo segundo. Trate dois tipos de erro:
# ValueError se o usuário digitar algo inválido
# ZeroDivisionError se tentar dividir por zero

try:
    dividendo: float = float(input("digite o dividendo: "))
    divisor: float = float(input("Digite o divisor: "))
    resultado: float = dividendo / divisor
    print(resultado)
except ValueError as e:
    print(f"{type(e).__name__}: Apenas números são permitidos.")
except ZeroDivisionError as e:
    print(f"{type(e).__name__}: Divisão por zero não é permitida.")