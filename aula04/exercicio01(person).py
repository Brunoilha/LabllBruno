#person

def new_dic():
    dic = {}
    
    dic['name'] = input("digite seu nome: ")
    
    dic["city"] = input("digite sua cidade: ")
   
    dic["age"] = int(input("digite sua idade: "))
    
    dic['sex'] = input("masculino ou feminino")
  
    dic["states"] = (input("qual estado brassilerio você é: "))
    return dic
    
def main():
    dic = new_dic()
    print(dic)
    
main()
