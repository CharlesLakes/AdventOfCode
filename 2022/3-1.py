import string
abc = string.ascii_lowercase + string.ascii_uppercase
archivo = open("input.txt")
suma = 0
for linea in archivo:
    n = len(linea)
    mitad = int((n - 1)/2)
    p1 = linea[:mitad + 1]
    p2 = linea[mitad + 1:]
    for a in p1:
        for b in p2:
            if(a == b):
                break
        if(a == b):
            break  
    i = abc.index(a) + 1
    suma += i
print(suma)      
archivo.close()