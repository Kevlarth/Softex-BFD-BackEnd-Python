# O programa deve receber o valor de uma compra e o valor pago pelo cliente.
# Calcular e mostrar o troco.

print("===== Calculadora de troco =====")
valor_compra = float(input("Digite qual o valor da compra: "))
valor_pagamento = float(input("Digite qual o valor do pagamento: "))

print("===== Valor do Troco =====")
if (valor_pagamento == 0) or (valor_pagamento == 0):
    print("Valor inválido, o valor da compra ou do pagamento deve ser diferente de zero ( 0 ).") 
elif (valor_pagamento < valor_compra):
    print("Valor inválido, o pagamento deve ter um valor maior ou igual ao valor da compra.")
else:
    print(f"Para uma compra de R$ {valor_compra}, com um pagamento de R$ {valor_pagamento} deve-se dá um troco no valor de {valor_pagamento-valor_compra}")
