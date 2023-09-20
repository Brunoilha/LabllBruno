matriz = [[5,8,0],[1,6,7],[2,4,3]]
for line in range(len(matriz)):
    for column in range(len(matriz[line])):
        min_line = line
        min_column = column
        for line_aux in range(line,len(matriz)):
            start = column if line == line_aux else 0
            for column_aux in range(start, len(matriz[line_aux])):
                if matriz[line_aux][column_aux] < matriz[min_line][min_column]:
                    min_line = line_aux
                    min_column = column_aux
        min_value = matriz[min_line][min_column]
        matriz[min_line][min_column] = matriz[line][column]
        matriz[line][column] = min_value
                
print(matriz)
