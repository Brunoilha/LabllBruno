#Invertendo uma Lista em Python sem Usar Métodos Internos

def reverse_array(array):
    array = [1,2,3,4,5]
    reverse = array[::-1]
    return reverse

def main():
    array = [1,2,3,4,5]
    reverse = reverse_array(array)
    print(array)
    print(reverse)

main()

