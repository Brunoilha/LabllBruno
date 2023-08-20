#Escreva uma função que recebe duas matrizes como entrada e retorna uma nova matriz que é a soma das duas matrizes. Ambas matrizes devem possuir o tamanho de 3 x 3.


def matriz_duo(matriz1,matriz2):
    new_matriz = []
    for line in range(len(matriz1)):
        new_line = []
        for element in range(len(matriz1[line])):
            value = matriz1[line][element] + matriz2[line][element]
            new_line.append(value)
        new_matriz.append(new_line)
    return new_matriz
                
def main():
    matriz1 = [[1,3,5],[7,9,11],[13,15,17]]
    matriz2 = [[2,4,6],[8,10,12],[14,16,18]]
    result = matriz_duo(matriz1,matriz2)
    print("nova matriz",result )
    
main()
