#Escreva uma função que verifica se uma matriz quadrada é simétrica, ou seja, se ela é igual à sua matriz transposta.
#tentei mas não bombou!

def transposed(matriz1,matriz2):
    for line in range(len(matriz1)):
        for column in range(len(matriz1[line])):
            for element in range(len(matriz2[line])):
                if matriz1[line][column] != matriz2[column][line]:
                    return False
                
    return True
    
def main():
    matriz1 = [[1,2,3],[4,5,6],[7,8,9]]
    matriz2 = [[1,2,3],[4,6,5],[7,9,8]]
    transposed(matriz1,matriz2)
    print(transposed(matriz1))
    print(transposed(matriz2))
    
main()
