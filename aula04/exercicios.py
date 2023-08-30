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


##2.Crie um dicionário vazio semana

def my_week():
    week = {}
    weeks = input("digite um dia da semana: ")
    
    if weeks == "monday":
        week[weeks] = "class: " + monday
        
    elif weeks == 'tuesday':
        week[weeks] = "class: " + tuesday
        
    elif weeks == "wednesday":
        week[weeks] = "class: " + wednesday
        
    elif weeks == "thursday":
        week[weeks] = "class: " + thursday
        
    elif weeks == "friday":
        week[weeks] = 'class: ' + friday
        
    else:
        week[weeks] = "não tenho aula nesse dia"
   
    return week
    
def main():
    week = my_week()
    print(week)
   
monday = "foil"
tuesday = "Laboratório de Algoritmos 2"
wednesday = "Inglês"
thursday = "Probabilidade e Estatística"
friday = "Fundamentos de Economia e Administração"
    
main()
