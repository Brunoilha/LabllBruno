1. Faç#a um programa para gerar automaticamente números entre 0 e 99 de uma cartela de bingo. Sabendo que cada cartela devera conter 5 linhas de 5 números, gere estes dados de modo a não ter números repetidos dentro das cartelas. O programa deve exibir na tela a cartela gerada.

import random
matriz = [[],[],[],[],[]]


for i in range(5):
    for j in range(5):
        matriz[i].append(random.randint(0,99))

print(matriz)
