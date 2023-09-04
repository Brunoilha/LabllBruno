#Escreva um programa que calcule e imprima a soma de todos os elementos abaixo da diagonal principal de uma matriz
def diagonelly(matriz):
    sum = 0
    n = len(matriz)

    for i in range(n):
        for j in range(i):  
            sum += matriz[i][j]

    return sum

def main():
    
    matriz = [[5,8,9],[3,4,7],[10,15,44]]
    
    result = diagonelly(matriz)
    print("A soma dos numeros embaixo da diagonel é:", result)
main()
