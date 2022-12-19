def reducir(lista):
    new_lista = []
    for linea in lista[1:]:
        _,s = linea.split(":")
        s = s.strip()
        if s.isnumeric():
            new_lista.append(int(s))
        else:
            new_lista.append(s)
    new_lista[0] = [new_lista[0]] if type(new_lista[0]) == int else list(map(int,new_lista[0].split(",")))
    new_lista[1] = new_lista[1].split("=")[1].strip()
    i = new_lista[2].index("by ") + 3
    new_lista[2] = int(new_lista[2][i:])
    i = new_lista[3].index("monkey ") + 7
    new_lista[3] = int(new_lista[3][i:])
    i = new_lista[4].index("monkey ") + 7
    new_lista[4] = int(new_lista[4][i:])
    return new_lista

archivo = open("input.txt")

data = archivo.read().split("\n\n")
data = list(map(lambda a: a.split("\n"),data))

aux = []

for linea in data:
    aux.append(reducir(linea))

times = [0 for _ in range(len(aux))]
print(aux)
for _ in range(20):
    print(_)
    for n,monkey in enumerate(aux):
        if len(monkey[0]) > 0:
            monkey[0] = list(map(lambda old: (eval(monkey[1])) // 3,monkey[0]))
            for m in monkey[0]:
                times[n] += 1
                if m % monkey[2] == 0:
                    aux[monkey[3]][0].append(m)
                else:
                    aux[monkey[4]][0].append(m)
            aux[n][0] = []
            
times.sort()

print(times[-1]*times[-2])
archivo.close()