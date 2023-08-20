#A partir de uma matriz 3 x 3 numérica, percorra a matriz e calcule o valor médio total da matriz e de cada linha

def average_matriz(matriz):
    total = 0 
    for line in range(len(matriz)):
        for content in range(len(matriz[line])):
            total += matriz[line][content] / 9
    return total   

def main():
    matriz = [[1,2,3],[4,5,6],[7,8,9]]
    result = average_matriz(matriz)
    print("a media dos valores é: ", result)
main()
