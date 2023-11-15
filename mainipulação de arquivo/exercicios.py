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
    file_word = input("Digite uma palavra: ")
    archive = open('file_words.txt', "r")

    line_number = 0
    for line in archive:
        line_number += 1
        if file_word in line:
            print(f"A palavra" ,file_word, "está no arquivo")
            print("esta na linha:", line_number)
            return True
            
    print(f"A palavra" ,file_word," não está no arquivo!")
    return False

def main():
    result = words()
    print(result)
main()

#3. Crie um programa que pede ao usuário para digitar o nome de um arquivo. Em
#seguida, o programa deve criar uma cópia desse arquivo com o nome
#"copia_nomeoriginal" (por exemplo, se o arquivo original for "exemplo.txt" , a cópia
#deve ser "copia_exemplo.txt").

def copy_file():
    name_file = input("Digite o nome do arquivo: ")
    
    try:
        archive = open(name_file + ".txt", "r")
        print("Cópia_" + name_file + ".txt")
    except FileNotFoundError:
        print(f"O arquivo" , name_file,".txt não foi encontrado.")
        archive.close()

def main():
    copy_file()

main()



