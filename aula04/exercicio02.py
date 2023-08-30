#1.Faça um dicionário com as 5 pessoas mais perto de você, tendo o nome como chave e a cor da camisa que está usando como valor. Após, imprima o resultado de forma amigável.

def dict():
    dic = {}
    for i in range(5):
        name = input("digite seu nome: ")
        dic[name] = input("digite a cor da peita: ")
    
    return dic
    
def main():
    dic = dict()
    print(dic)
    
main()
