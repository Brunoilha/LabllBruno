

import random


def termo_game(attempt, guess):
    termo = open('palavras.txt', "r")
    content = termo.read()
    split_content = content.split()
    drawn = random.choice(split_content)
    file = open('palavras_escolhidas.txt', "a")
    file.write(drawn)
    used_words = open('palavras_escolhidas.txt', 'r')
    reading_used_words = used_words.read()
    splited_used_words = reading_used_words.split()

    repeated_words = []
    


    if drawn not in splited_used_words:
        while attempt != 0:
            try:
                guess = []
                var = -1
                word = input(f"\033[1;36;1m Digite uma palavra: \033[m").lower()

                if len(word) != 5:
                    raise TypeError(f"\033[1;36;1m Mais louco que o Batman? Digite uma palavra com 5 letras\033[m")

                if " " in word:
                    raise TypeError(f"\033[1;36;1m Aí não meu consagrado, digite sem espaços\033[m")

                if word in repeated_words:
                    raise TypeError(f"\033[1;36;1m A mesma palavra? Aí tu ta sem criatividade meu nobre\033[m")

                if "0" in word or "1" in word or "2" in word or "3" in word or "4" in word or "5" in word or "6" in word or "7" in word or "8" in word or "9" in word:
                    raise TypeError(f"\033[1;36;1m Palavra com número? aqui não doutor! \033[m")


                if 'á' in word or 'à' in word or 'ã' in word or 'â' in word or 'é' in word or 'è' in word or 'ê' in word or 'í' in word or 'ì' in word or 'î' in word or 'ó' in word or 'ò' in word or 'õ' in word or 'ô' in word or 'ú' in word or 'ù' in word or 'û' in word or 'ç' in word:
                    raise TypeError("\033[1;36;1m Palavra com Acento? aqui não príncipe \033[m")


                if word == drawn:
                    print(f"\033[1;36;1m PARABÉNS VOCÊ ACERTOU!!\033[m")

                    break
                else:
                    for letter in range(len(word)):
                        var = var + 1
                        if word[letter] == drawn[letter]:
                            guess.insert(var, f"\033[1;32;1m {word[letter]}")
                        elif word[letter] in drawn:
                            guess.insert(var, f"\033[1;33;1m {word[letter]}")
                        else:
                            guess.insert(var, f"\033[1;37;1m {word[letter]}")
                    string_guess = "".join(guess)
                    print(f"\033[1;36;1m Palavra: {string_guess}\033[m")
                    attempt = attempt - 1
                    print(f"\033[1;36;1m Você tem {attempt} restante(s)\033[m")
                    repeated_words.append(word)
                if attempt == 0:
                    print(f"\033[1;36;1m JOGOU COMO NUNCA PERDEU COMO SEMPRE, A PALAVRA ERA:\033[m", drawn)

            except IndexError:
                print(f"\033[1;36;1m Tente novamente meu chapa! \033[m")

            except ValueError:
                print(f"\033[1;36;1m Digite uma palavra!!!\033[m")

            except BaseException as error:
                print(f"\033[1;36;1m {error}\033[m")

    else:
        drawn = random.choice(split_content)
