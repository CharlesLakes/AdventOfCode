archivo = open("input.txt")

def es_visible(m,x,y):
    if(x == 0 or y == 0 or y == len(m) - 1 or x == len(m[y]) - 1):
        return True

    status1 = True
    for i in range(0,x):
        if m[y][x] <= m[y][i]:
            status1 = False
            break
    status2 = True
    for i in range(x + 1,len(m[y])):
        if m[y][x] <= m[y][i]:
            status2 = False
            break
    status3 = True
    for i in range(0,y):
        if m[y][x] <= m[i][x]:
            status3 = False
            break
    status4 = True
    for i in range(y + 1,len(m)):
        if m[y][x] <= m[i][x]:
            status4 = False
            break

    return status1 or status2 or status3 or status4

data = list(map(lambda e: list(map(int,list(e))),archivo.read().split("\n")))


c = 0
for y in range(len(data)):
    for x in range(len(data[y])):
        if(es_visible(data,x,y)):
            print(x,y,data[y][x])
            c += 1
print(c)
archivo.close()