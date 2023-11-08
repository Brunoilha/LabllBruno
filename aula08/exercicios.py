#2. sistema com numero de 0 a 10 usando assert/AssertionError

def get_numbers(number):
        numbers = ("0","1","2","3","4","5","6","7","8","9","10")
      
def main():
    try:
        number = int(input("digite um numero: "))
        result = get_numbers(number)
        assert number >= 0 and number <= 10
        print("o numero",number, "é valido!")

    except ValueError:
        print("[error] o valor digitado não está no sistema!")
    except AssertionError:
        print("[error] somente de 0 a 10")
    
main()

#4. Crie uma função chamada find_element que aceita uma lista e utilizar IndexError

def find_element(element):
    try:
        elements = ("água","fogo","ar","terra","raio","sombrio","luz","escuridão","psiquico")
        return elements[element - 1]
    except IndexError:
        print("o numero", element, "é invalido!")

def main():
    try:
        element = int(input("digite um nuemro para encontrar um elemento: "))
        result = find_element(element)
        print("o elemento que voce achou é:", result)
    except ValueError:
        print("digite novamente, opçao invalida!")
        
main()

#3 Escreva uma função calculate_square_root que aceite um número como entrada e retorne a raiz quadrada desse número.

class Negative(BaseException):
    pass

def calculate_square_root(number):
    source = number ** (1/2)
    print(source)

def main():
    number = int(input("digite um numero: "))
    result = calculate_square_root(number)
    print("o valor da raiz quadrada de", number, "é", result)
    
    
main()
