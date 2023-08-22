#Crie um método que receba uma lista com elementos duplicados. Ela deve gerar uma lista com os elementos que estava duplicados e uma lista com os elementos unificados
def double_list(list, new_list):
    for i in list:
        if i not in new_list:
            new_list.append(i)
        return new_list, list
def main():
    list = []
    new_list = []
    for i in range(10):
        n = float(input("digite um numero:"))
        list.append(n)
    new_list,list = double_list(list, new_list)
    print("lista:", list)
    print("nova lista: ", new_list)
    
main()
