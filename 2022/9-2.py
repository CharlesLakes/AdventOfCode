def detect(pca,pco):
    return abs(pco[0] - pca[0]) <= 1 and abs(pco[1] - pca[1]) <= 1


def alrededor(p):
    l = []
    for i in range(0,3):
        l.append((p[0] - 1,p[1] + i - 1))
        l.append((p[0] + 1,p[1] + i - 1))
    l.append((p[0],p[1] + 1))
    l.append((p[0],p[1] - 1))
    return l

def mas_cercano(l,p):
    i = -1
    last = float("inf")
    for j,e in enumerate(l):
        if ((l[j][0] - p[0])**2 + (l[j][1] - p[1])**2)**0.5 < last:
            last = ((l[j][0] - p[0])**2 + (l[j][1] - p[1])**2)**0.5
            i = j
    return l[i]

archivo = open("input.txt")

visitadas = [(0,0)]
cola = [(0,0) for _ in range(10)]


data = archivo.read().split("\n")
data = list(map(lambda a: (a.split(" ")[0],int(a.split(" ")[1])),data))


for d,c in data: 
    
    for i in range(c):
        if d == "R":
            cola[0] = (cola[0][0] + 1,cola[0][1])
        elif d == "U":
            cola[0] = (cola[0][0],cola[0][1] + 1)
        elif d == "L":
            cola[0] = (cola[0][0] - 1,cola[0][1])
        elif d == "D":
            cola[0] = (cola[0][0],cola[0][1] - 1)


        for j in range(1,10):
            if not detect(cola[j],cola[j - 1]):
                temp = list(filter(lambda a: detect(a,cola[j - 1]),alrededor(cola[j])))
                cola[j] = mas_cercano(temp,cola[j - 1])
                if j == 9:
                    visitadas.append(cola[j])
            else:
                break
        print(cola)

print(len(set(visitadas)))
archivo.close()