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

#3.Crie um dicionário vazio filmes

def movies_top():
    my_movies = {"spider man": "2014 and green elf","interstellar": "2014 and paradox","star wars": "1999 and darth vader","ben ten": "2005 and vilgax",
    "batman the dark knight": "2008 and joker"}

    opc = ""
    while opc != "-1":
        print("Escolha um filme:")
        for movie in my_movies:
            print(movie)
        opc = input("Digite o nome do filme ou -1 para sair: ")
        
        if opc in my_movies:
            print("Ano e vilão:", {my_movies[opc]})
        else:
            print("Tente novamente!")

def main():
    movies_top()

main()

#4.Escreva um programa em Python que verifique se uma chave existe ou não em um dicionário. Se a chave existir no dicionário, imprima Verdadeiro. Caso contrário, imprima Falso.

def keys_t_or_f():
    dic = {"carro", "trem","moto", "ceu", "chuva"}
    result = []
    for i in range(5):
        x = input("digite uma chave: ")
        if x in dic:
            result.append(True)
        else:
            result.append(False)
    return result
def main():
    result = keys_t_or_f()
    print(result)
    
main()
#5.Escreva uma função que conta a quantidade de vogais em um texto e armazena tal quantidade em um dicionário, onde a chave é a vogal considerada.
    
def vowel(dict,count_a,count_e,count_i,count_o,count_u):
    word = input("digite algo: ")
    for i in word:
        for x in i:
            
            if x == "a":
                count_a = count_a + 1
                dict["a"] = count_a
                
            elif x == "e":
                count_e = count_e + 1
                dict["e"] = count_e
            
            elif x == "i":
                count_i = count_i + 1 
                dict["i"] = count_i
            
            elif x == "o":
                count_o = count_o + 1
                dict["o"] = count_o
            
            elif x == "u":
                count_u = count_u + 1
                dict["u"] = count_u
    return dict
    
def main():
    dict = {}
    count_a = 0
    count_e = 0 
    count_i = 0
    count_o = 0
    count_u = 0 
    dict = vowel(dict,count_a,count_e,count_i,count_o,count_u)
    print("vogais total: ", (dict))
    
main()

#6.Escreva um programa que lê duas notas de vários alunos e armazena tais notas em um dicionário é o nome do aluno. A entrada de dados deve terminar quando for lida uma string vazia como nome. Escreva uma
#função que retorna a média do aluno, dado seu nome.


def note_students(note):
    total = sum(note)
    average = total / len(note)
    return average
    
def main():
    students_note = {}
    name = input("digite um nome: ")
    note1 = float(input("digite a nota do aluno: "))
    note2 = float(input("digite a nota do aluno: "))
    
    students_note[name] = [note1,note2]
    
    if name in students_note:
        average = note_students(students_note[name])
        print("o(a)" , name,  "tirou a media:", average)
    else:
        print("aluno inexistente!!")
        
main()
        
