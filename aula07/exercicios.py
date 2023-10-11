
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
