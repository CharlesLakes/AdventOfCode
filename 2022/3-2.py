import string
abc = string.ascii_lowercase + string.ascii_uppercase
archivo = open("input.txt")
suma = 0
co = 0
last = []
for linea in archivo:
    n = len(linea)
    co += 1

    if(co == 3):
        for a in linea:
            for b in last[0]:
                for c in last[1]:
                    if a == b == c:
                        break
                if a == b == c:
                    break
            if a == b == c:
                break
        #print(a)
        suma += abc.index(a) + 1
        co = 0
        last = []

    else:
        last.append(linea)
print(suma)     
archivo.close()