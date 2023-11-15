#1. Crie um arquivo contendo uma lista de números separados por vírgulas. Escreva
#um programa que lê esses números do arquivo e calcula a média deles.

def calculate_avg():
    my_file = open('file_numbers.txt', "r")
    file_content = my_file.read()
    file_list = file_content.split(',')
    sum_of_numbers = 0 
    for number in file_list:
        sum_of_numbers += int(number) 
    return print(sum_of_numbers / len(file_list))
    
def main():
    result = calculate_avg()
    print(result)
    
main()

##2. Crie um arquivo de texto contendo várias linhas de texto. Escreva um programa
#que solicita ao usuário uma palavra e verifica se essa palavra está presente no
#arquivo. Se estiver, o programa deve imprimir a linha em que a palavra foi
#encontrada.
def words():
    file_word = input("digite uma palavra: ")
    archive = open('file_words.txt', "r")
    search = archive.readline()
    line = 0 
    for search in file_word:
        if file_word == archive:
            True    
        else:
            False
    search = archive.readline()

def main():
    words()
    
main()
