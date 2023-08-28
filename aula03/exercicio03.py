##notas 
contador100 = 0
contador50 = 0
contador20 = 0
contador10 = 0 
saque = int(input("digite o valor do saque: "))
while saque > 0:
    
    if saque >= 100:
        saque -= 100
        contador100 += 1
    
    elif saque >= 50:
        saque -= 50
        contador50 += 1
    
    elif saque >= 20:
        saque -= 20 
        contador20 += 1
    
    elif saque >= 10:
        saque -= 10 
        contador10 += 1

print("notas de 100", contador100, "notas de 50", contador50, "notas de 20", contador20, "notas de 10", contador10 )
