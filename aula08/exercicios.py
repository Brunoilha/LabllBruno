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
    if number < 0:
        raise Negative(f"[error] não é permitido numeros negativos!")
    source = number ** (1/2)
    print(source)

def main():
    try:
        number = int(input("digite um numero: "))
        result = calculate_square_root(number)
        print("o valor da raiz quadrada de", number, "é", result)
    except Negative as error:
        print(error)
    
main() 

 #1 - Crie um método para verificar se um triângulo é equilátero (todos os lados iguais),
#isósceles (dois lados iguais) ou escaleno (todos lados diferentes). Se os lados não
#formarem um triângulo válido (se a soma de dois lados for menor que o terceiro lado),
#lance uma exceção ValueError utilizando a cláusula raise com uma mensagem
#indicando que o triângulo informado é inválido.

class sum_triangle(BaseException):
    pass

def get_triangle(triangle1,triangle2,triangle3):
    triangles_type1 = "equilatero"
    triangles_type2 = "isoceles"
    triangles_type3 = "escaleno"
    
    if triangle1 == triangle2 == triangle3:
        print("seu triangulo é ", triangles_type1)
        
    elif triangle1 != triangle2 != triangle3:
        print("seu triangulo é:", triangles_type3)
        
    elif triangle1 == triangle2 != triangle3 or triangle1 == triangle3 != triangle2 or triangle1 != triangle2 == triangle3:
        print("seu triangulo é:", triangles_type2)
    else:
        print("tente novamente")
        
def main():
    try:
        triangle1 = int(input("digite qual o valor do lado do triangulo: "))
        triangle2 = int(input("digite qual o valor do lado do triangulo: "))
        triangle3 = int(input("digite qual o valor do lado do triangulo: "))
        if triangle1 + triangle2 < triangle3 or triangle1 + triangle3 < triangle2 or triangle2 + triangle3 < triangle1:
            raise sum_triangle(f"[error] triangulo informado é invaldo!")
        result = get_triangle(triangle1,triangle2,triangle3)
        print(result)
    except ValueError:
        print("[error] tente novamente")
    except sum_triangle as error:
        print(error)
    
main()
