archivo = open("input.txt")

def puntuacion(m,x,y):
    p1 = 0
    p2 = 0
    p3 = 0
    p4 = 0
    for i in range(x - 1,-1,-1):
        p1 += 1
        if m[y][x] <= m[y][i]:
            break
            
    for i in range(x + 1,len(m[y])):
        p2 += 1
        if m[y][x] <= m[y][i]:
            break
            
    for i in range(y - 1,-1,-1):
        p3 += 1
        if m[y][x] <= m[i][x]:
            break

    for i in range(y + 1,len(m)):
        p4 += 1
        if m[y][x] <= m[i][x]:
            break

    return p1*p2*p3*p4

data = list(map(lambda e: list(map(int,list(e))),archivo.read().split("\n")))

c = 0
for y in range(len(data)):
    for x in range(len(data[y])):
        temp = puntuacion(data,x,y)
        if temp > c:
            c = temp
print(c)
archivo.close()