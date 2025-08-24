"""
11- Usando list comprehension, crie um tabuleiro de xadrez vazio e depois adicione todas as peças do jogo na posição inicial.
Para melhorar a visualização do tabuleiro, identifique as posições do tabuleiro da seguinte forma:

    [ ] - para posições vazias
    tor - para a torre
    cav - para o cavalo
    bis - para o bispo
    rai - para a rainha
    rei - para o rei
    pea - para o peão

Por fim imprima o tabuleiro na tela, deixando cada linha da matriz abaixo da outra. (Dica você pode usar a biblioteca numpy para auxiliar na impressão da matriz)
"""


TABULEIRO: list[list] = [[] for x in range(8) for _ in range(8)]
PEÇAS: list[str] = ["tor","cav","bis","rai","rei","bis","cav","torre","pea","pea","pea","pea","pea","pea","pea","pea"]
for i in range(len(PEÇAS)):
    TABULEIRO[i] = PEÇAS[i]
for j in range(0, len(TABULEIRO), 8):
    print(TABULEIRO[j:j+8])