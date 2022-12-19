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

archivo = open("input.txt")
data = [list(map(int,e.split(","))) for e in archivo.read().strip().split("\n")]

suma = len(data)*6
past = []

for x,y,z in data:
    temp = buscar((x,y,z),past)
    if temp:    
        suma -= temp*2
    past.append((x,y,z))

print(suma)

archivo.close()
