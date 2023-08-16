#Crie um método que receba uma lista com elementos duplicados. Ela deve gerar uma lista com os elementos que estava duplicados e uma lista com os elementos unificados
def double_list(array, new_list):
    for i in array:
        if i not in new_list:
            new_list.append(i)
def main():
    array = []
    new_list = []
    for i in range(10):
        n = float(input("digite um numero:"))
        array.append(n)
    double_list(array, new_list)
    print("lista:", array)
    print("nova lista: ", new_list)
    
main()
