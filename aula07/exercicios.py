#Crie um programa que receba através de input dois números e retorne sua divisão.
def division(num1,num2):
     try:
        return num1 / num2
    except ZeroDivisionError:
        print('[erro] voce nao pode dividir um numero por zero')
    except BaseException as error:
        print(f'[erro] ocorreu um erro: {error} ')
        
def int_input(message):
    while True:
        try:
            value = int_input(message)
            return value
        except ValueError:
            print('[erro] o numero digitade é invalido')
        except BaseException as error:
            print(f'[error] ocorreu um erro: {error} ')
        
def main():
    try:
        num1  = int_input('digite um valor para n1')
        num2  = int_input('digite um valor para n2')
        result = division(num1,num2)
        print("resultado", result )
    
    except ValueError:
        print('[erro] o numero digitade é invalido')
    except BaseException:
        print(f'[error] ocorreu um erro: {erro} ')
            
main()

#Crie um programa que receba através de um input o valor numérico de um mês e retorne seu valor escrito. Lembre de tratar as exceções do seu programa. Exemplo: 1 -> Janeiro, 12 -> Dezembro
class InvalidMonthError(BaseException):
    pass 
class InvalidMonthError(BaseException):
    pass 
def get_month(month):
    try:
        months = ("janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro")
        return months[month -1]
    except IndexError:
        print('[error] tente novamente com numeros inteiros')
    except BaseException as error:
        print(f'[erro] ocorreu um erro: {error} ')

def main():
    try:
        month = int(input("digite um numero para saber o mes conrrespondete: "))
        if month > 12 or month < 1:
            raise InvalidMonthError
        month_name = get_month(month)
        print(f'o mes é:{month_name} ')
    except ValueError:
        print('[erro] tente novamente com numeros inteiros')
    except InvalidMonthError:
        print('[error] o mes informado nao existe')
    except BaseException as error:
        print(f'[erro] ocorreu um erro: {error} ')
        
main()
    
    
    
    
