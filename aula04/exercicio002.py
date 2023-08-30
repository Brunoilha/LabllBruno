#Crie uma função que receba uma frase e retorne em um objeto as letras com a quantidade de vezes com que ela
está presente na frase.
def words(my_list):
   dic = {}
   
   
   for word in my_list:
       for letters in word:
            if letters in dic:
                dic[word] += 1 
            else:
                dic[word] += 1 
       
def main():
    my_list = "allops"
    
    result = words(my_list)
    
main()
    
