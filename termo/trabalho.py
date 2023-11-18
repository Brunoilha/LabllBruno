import random

def termo_game():
    termo = open('palavras.txt',"r")
    content = termo.readlines()
    drawn = random.choice(content)
    print(drawn)
    
    tentative = input("digite uma palavra: ")
    c = 0 
    for x in  tentative:
        c += 1
        contador = 0
        for y in drawn:
            contador += 1 
            if c == contador and x == y:
                print("verde")
            elif y in tentative:
                print("amarelo")
            else:
                print("branco")
                
def main():
    termo_game()
    

main()
