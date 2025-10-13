# Crie uma interface chamada Pagamento com um método abstrato processar(valor).
# Depois, crie duas classes (CartaoCredito e Boleto) que implementem a interface.
# Mostre como chamar processar() para cada uma.

from abc import ABC, abstractmethod
from decimal import Decimal

class IPagamento():
    @abstractmethod
    def processar(self, valor: Decimal):
        ...

class CartaoCredito(IPagamento):
    def processar(self, valor: Decimal):
        print(f"Pagamento via cartão de crédito no valor de R$ {valor} efetivado!")

class Boleto(IPagamento):
    def processar(self, valor):
        print(f"Pagamento via boleto no valor de R$ {valor} efetivado!")

tivro_card: CartaoCredito = CartaoCredito()
tivro_card.processar(402.99) 

folha_a4: Boleto = Boleto()
folha_a4.processar(199.31)