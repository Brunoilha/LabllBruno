#Escreva uma função que recebe uma lista de números e crie um dicionário que seja estruturado como sendo o número a chave e a quantidade de vezes que o número está presente o valor.
def number(my_list):
   dic = {}
   
   
   for number in my_list:
       if number in dic:
           dic[number] += 1 
        else:
            dic[number] += 1 
       
       
       
def main():
    my_list = [1,2,3,4,5,5,3]
    
    result = number(my_list)
    
main()
    
    
