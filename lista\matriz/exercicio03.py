#A partir de uma matriz 3 x 3 numérica, percorra a matriz e some os maiores valores de cada linha
def value_matriz(matriz):
    total = 0 
    for line in range(len(matriz)):
        value_max = [line][0]
        for value in matriz[line]:
            if value > value_max:
                value_max = value
        total += value_max
    return total
        
def main():
    matriz = [[1,2,3], [4,5,6], [7,8,9]]
    resutl = value_matriz(matriz)
    print("valor toal da linha: ", resutl)
    
main()
