#Imagine que você está criando um programa para gerenciar o estoque de produtos em uma loja. Você pode usar um dicionário para rastrear os produtos, suas quantidades e preços.

def menu():
    print("1 - add produto")
    print("2 - buscar produto")
    print("3 - vizualisar todos os produtos")
    print("4 - vender produto")
    print("5 - relatorio de vendas")
    print("6 - sair")
    opt = int(input("digite uma opt: "))
    return opt

def add_product(my_dict,historic_all):
    name_product = input("digite o nome de algum produto: ").upper()
    category = input("digite a categoria do produto adicionado: ").upper()
    
    if name_product not in my_dict:
        value = float(input("digite o valor do seu produto: "))
        values_list.append(value)
        amount = int(input("digite quantos deseja adicionar no estoque: "))
        my_dict[name_product] = {"value": value, "amount": amount, "category": category}
        historic_all[name_product] = {"amount update" = [amount], "value update" [value]}
        print("seu produto foi adicionado com sucesso")
    else:
        print("o produto ja esta em estoque!, quantos voce gostaria de adicionar? ")
        amount = int(input("digite a quantidade que voce deseja adicionar a mais: "))
        my_dict[name_product]["amount"] = my_dict[name_product]["amount"] + amount
        historic_all[name_product]["amount update"].append(my_dict[name_product]["amount"])
    return my_dict,values_list, historic_all
    
def search_product(my_dict):
    name_product = input("qual produto deseja buscar: ").upper()
    
    if name_product in my_dict:
        print("produto:" , name_product)
        print("valor:" , my_dict[name_product]["value"])
        print("estoque:", my_dict[name_product]["amount"])
        print("categoria:", my_dict[name_product]["category"])
    else:
        print("o ", name_product, "nao foi buscado")
        
def sell_product(my_dict,my_dict2,historic_all):
    sell_quantity = 0
    value_total = 0
    name_product = input("qual produto deseja vender: ").upper()
    if name_product in my_dict:
        sell = int(input("quantos produtos voce gostaria de vender?"))
        if sell <= my_dict[name_product]["amount"] :
            
            my_dict[name_product]["amount"] -= sell
            price_total = my_dict[name_product]["value"] * sell
            historic_all[name_product]["amount update"].append(my_dict[name_product]["amount"])
            print("o valor total foi de:", price_total)
            
            if name_product not in my_dict2:
                my_dict2[name_product] = {"quantidade vendida": sell, "total do valor vendido": price_total}
            else:
                my_dict2[name_product]["quantidade vendida"] += sell
                my_dict2[name_product]["total do valor vendido"] += price_total
        else:
            print("esse produto esta em falta no estoque")
    else:
        print("esse produto não encontra-se no estoque!")
    return my_dict, my_dict2,historic_all
    
def sales_report(my_dict,my_dict2):
    print(my_dict2)
    # continua...
def change_value(my_dict,historic_all):
    name_product = input("digite o nome do produto que deseja alterar o valor: ")
    new_value = float(input("digite um novo valor para o produto: "))
    my_dict[name_product]["value"] = new_value
    values_list.append(new_value)
    historic_all[name_product]["value update"].append(new_value)
    return my_dict,values_list,historic_all
    
def dell_product(my_dict,historic_all):
     name_product = input("digite o nome do produto que deseja deletar: ")
     my_dict.pop(name_product)
     historic_all[name_product]["deleted products"] = []
     historic_all[name_product]["deleted products"].append(name_product)
     return my_dict,historic_all
     
    
    
def main():
    historic_all = {}
    values_list = []
    my_dict = {}
    my_dict2 = {}
    while True:
        opt = menu()
        if opt == 1:
            my_dict = add_product(my_dict)
        elif opt == 2:
            search_product(my_dict)
        elif opt == 3:
            print(my_dict)
        elif opt == 4:
            my_dict,my_dict2 = sell_product(my_dict,my_dict2)
        elif opt == 5:
            sales_report(my_dict,my_dict2)
        elif opt == 6:
            break
    
main()
