archivo = open("input.txt")
contador = 0
for linea in archivo:
    e1,e2 = linea.split(",")
    i1,j1 = list(map(int,e1.split("-")))
    i2,j2 = list(map(int,e2.split("-")))
    #print(i1,j1,i2,j2)
    if(i1 <= i2 <= j1 or i1 <= j2 <= j1):
        contador += 1
    elif(i2 <= i1 <= j2 or i2 <= j1 <= j2):
        contador += 1
print(contador)
archivo.close()