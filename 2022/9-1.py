def detect(pca,pco):
    return abs(pco[0] - pca[0]) <= 1 and abs(pco[1] - pca[1]) <= 1

archivo = open("input.txt")

visitadas = [(0,0)]
posicion_cola = (0,0)
posicion_cabeza = (0,0)

data = archivo.read().split("\n")
data = list(map(lambda a: (a.split(" ")[0],int(a.split(" ")[1])),data))


for d,c in data: 
    
    for i in range(c):
        temp = posicion_cabeza
        if d == "R":
            posicion_cabeza = (posicion_cabeza[0] + 1,posicion_cabeza[1])
        elif d == "U":
            posicion_cabeza = (posicion_cabeza[0],posicion_cabeza[1] + 1)
        elif d == "L":
            posicion_cabeza = (posicion_cabeza[0] - 1,posicion_cabeza[1])
        elif d == "D":
            posicion_cabeza = (posicion_cabeza[0],posicion_cabeza[1] - 1)

        if not detect(posicion_cabeza,posicion_cola):
            posicion_cola = temp
            visitadas.append(temp)

print(len(set(visitadas)))
archivo.close()