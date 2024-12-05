
dag = []

while True:
    try:
        line = input().strip().split("|")
        dag.append([int(line[0]),int(line[1])])
        if len(line) == 0:
            break
    except:
        break

print(len(dag))
for p in dag:
    print(*p)

listas = []
while True:
    try:
        line = input().strip().split(",")
        line = list(map(int,line))
        listas.append(line)
    except:
        break

print(len(listas))
for lista in listas:
    print(len(lista))
    print(*lista)
