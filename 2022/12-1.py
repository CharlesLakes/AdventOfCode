def buscar_letrar(lista,letra):
    for j in range(len(lista)):
        for i in range(len(lista[j])):
            if lista[j][i] == letra:
                return (i,j)

def posibles_vecinos(usados,lista,pos):
    x,y = pos
    posibles = []
    if x > 0:
        posibles.append((x - 1,y))
    if y > 0:
        posibles.append((x,y - 1))
    if len(lista) - 1 > y:
        posibles.append((x,y + 1))
    if len(lista[y]) - 1 > x:
        posibles.append((x + 1,y))
    posibles = list(filter(
        lambda a: not usados[a[1]][a[0]] and ord(lista[y][x]) + 1 >= ord(lista[a[1]][a[0]]),
        posibles
    ))

    return posibles

archivo = open("input.txt")

data = archivo.read().split("\n")
data = list(map(lambda temp: list(temp),data))


usados = [[False for _ in range(len(data[0]))] for _ in range(len(data))]
S = buscar_letrar(data,"S")
E = buscar_letrar(data,"E")
usados[S[1]][S[0]] = True
data[S[1]][S[0]] = "a"
data[E[1]][E[0]] = "z"

actuales = [S]
c = 0
while len(actuales) > 0:
    temp = []
    for x,y in actuales:
        if (x,y) == E:
            print(c)
            exit()
        aux = posibles_vecinos(usados,data,(x,y))
        for i,j in aux:
            usados[j][i] = True
        temp += aux
    actuales = temp
    print(temp)
    c += 1
    



archivo.close()