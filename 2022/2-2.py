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
    if(b == "X"):
        if(a == "A"):
            suma += c["Z"]
        elif(a == "B"):
            suma += c["X"]
        elif(a == "C"):
            suma += c["Y"]
    elif(b == "Y"):
        suma += 3
        if(a == "A"):
            suma += c["X"]
        elif(a == "B"):
            suma += c["Y"]
        elif(a == "C"):
            suma += c["Z"]   
    elif(b == "Z"):
        suma += 6
        if(a == "A"):
            suma += c["Y"]
        elif(a == "B"):
            suma += c["Z"]
        elif(a == "C"):
            suma += c["X"] 
    #print(suma)
print(suma)
archivo.close()