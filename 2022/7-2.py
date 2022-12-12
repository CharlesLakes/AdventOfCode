archivo = open("input.txt")

result = []

def recur(puntero):
    size = 0
    #print(puntero[1:])
    for elemento in puntero[1:]:
        if not elemento:
            continue
        if type(elemento) == dict:
            k = list(elemento.keys())[0]
            size += recur(elemento[k])
        else:
            size += int(elemento[0])
    result.append(size)
    return size

mapeo = [
    None
]
puntero = None
data = archivo.read().split("\n")
for i in range(len(data)):
    aux = data[i].split(" ")
    if aux[0] == "$":
        if aux[1] == "cd":
            if aux[2] == "/":
                puntero = mapeo
            elif aux[2] == "..":
                puntero = puntero[0]
            else:
                #print(mapeo)
                for elemento in puntero:
                    if type(elemento) == dict and aux[2] in elemento:
                        puntero = elemento[aux[2]]
        elif aux[1] == "ls":
            j = i + 1
            aux1 = data[j].split(" ")
            while aux1[0] != "$" and j < len(data):
                if aux1[0] == "dir":
                    puntero.append({aux1[1]:[puntero]})
                else:
                    puntero.append((aux1[0],aux1[1]))
                    #print(puntero[1:])
                j += 1
                if j < len(data):
                    aux1 = data[j].split(" ")

libre = 70000000 - recur(mapeo)
falta = 30000000 - libre
result.sort()
for r in result:
    if falta <= r:
        print(r)
        break
archivo.close()