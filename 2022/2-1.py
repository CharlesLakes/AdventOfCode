archivo = open("input.txt")
c = {
    "X":1,
    "Y":2,
    "Z":3
}
data = archivo.read()
data = data.split("\n")
suma = 0
for linea in data:
    a,b = linea.split(" ")
    if((a == "A" and b == "X") or (a == "B" and b == "Y") or (a == "C" and b == "Z")):
        suma += 3 + c[b]
    else:
        if(a == "A"):
            if(b == "Y"):
                suma += 6 + c[b]
            else:
                suma += c[b]
        elif(a == "B"):
            if(b == "Z"):
                suma += 6 + c[b]
            else:
                suma += c[b]
        elif(a == "C"):
            if(b == "X"):
                suma += 6 + c[b]
            else:
                suma += c[b]
    #print(suma)
print(suma)
archivo.close()
