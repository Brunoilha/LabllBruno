def menu():
    try:
        print(f"\033[1;36;1m 1 - JOGAR TERMO\033[m")
        print(f"\033[1;36;1m 2 - RESETAR PALAVRAS UTILIZADAS!\033[m")
        print(f"\033[1;36;1m 3 - SAIR\033[m")
        opc = int(input(f"\033[1;36;1m Digite a opção desejada: \033[m"))
        return opc
    except ValueError:
        print(f"\033[1;36;1m Digite um número de 1 a 3 meu consagrado\033[m")
