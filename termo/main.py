
def main():
    from menu_termo import menu 
    from game_termo import termo_game
    
    file = open('palavras_escolhidas.txt', "w")
    attempt = 5
    guess = []
    opc = 0
    
    while opc != 3:
        opc = menu()
        if opc == 1:
            print(f"\033[1;36;1m BEM-VINDO AO JOGO TERMO!\033[m")
            termo_game(attempt, guess)
        elif opc == 2:
            f = open('palavras_escolhidas.txt',"w")
            f.close()
            print(f"\033[1;36;1m PALAVRAS RESETADAS COM SUCESSO! MEU REI!")
            
        elif opc == 3:
            print(f"\033[1;36;1m DO INGLÊS FAREWELL, PARA OS LEIGOS ADEUS!")
            break

main()
