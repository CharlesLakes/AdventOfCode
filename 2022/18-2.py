def es_adyacente(cord1,cord2):
    x1,y1,z1 = cord1
    x2,y2,z2 = cord2
    x3,y3,z3 = abs(x2 - x1),abs(y2 - y1),abs(z2 - z1)

    if x3 == 1 and y3 == z3 == 0:
        return True
    if y3 == 1 and x3 == z3 == 0:
        return True
    if z3 == 1 and x3 == y3 == 0:
        return True
    return False


def buscar(cord,db):
    count = 0
    for c in db:
        if es_adyacente(c,cord):
            print(c,cord)
            count += 1
    return count

def limites(cords):
    xs = []
    ys = []
    zs = []

    for c in cords:
        x,y,z = c
        xs.append(x)
        ys.append(y)
        zs.append(z)

    return max(xs),max(ys),max(zs)

def recur(cord,cords,marcados,maxs):
    x,y,z = cord
    marcados.append((x,y,z))
    
    if x + 1 < maxs[0] and (x + 1,y,z) not in marcados:
        recur((x + 1,y,z),cords,marcados,maxs)

    if y + 1 < maxs[1] and (x,y + 1,z) not in marcados:
        recur((x,y + 1,z),cords,marcados,maxs)
    
    if z + 1 < maxs[2] and (x,y,z + 1) not in marcados:
        recur((x,y,z + 1),cords,marcados,maxs)

    if x - 1 >= 0 and (x - 1,y,z) not in marcados:
        recur((x - 1,y,z),cords,marcados,maxs)

    if y - 1 >= 0 and (x,y - 1,z) not in marcados:
        recur((x,y - 1,z),cords,marcados,maxs)

    if z - 1 >= 0 and (x,y,z - 1) not in marcados:
        recur((x,y,z - 1),cords,marcados,maxs)
        

archivo = open("input.txt")
data = [list(map(int,e.split(","))) for e in archivo.read().strip().split("\n")]

suma = len(data)*6
past = []
marcados = []


maxs = limites(data)
recur((0,0,0),data,marcados,maxs)



"""
for x,y,z in data:
    temp = buscar((x,y,z),past)
    if temp:    
        suma -= temp*2
    past.append((x,y,z))

print(suma)
"""
archivo.close()
