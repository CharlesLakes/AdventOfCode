archivo = open("input.txt")
data = archivo.read().split('\n')
i = data.index('')
n = int(data[i - 1].replace(" ","")[-1])
pilas = [[] for _ in range(n)]
for j in range(i - 1):
    for k in range(n):
        inicial = 4*k
        final = inicial + 2
        if(data[j][inicial:final + 1] != "   "):
            pilas[k].append(data[j][inicial:final + 1])
for j in range(n):
    pilas[j].reverse()
for q in range(i + 1,len(data)):
    temp = data[q].replace("move","").replace("from","").replace("to","")[1:].split("  ")
    a,b,c = list(map(int,list(temp)))
    for _ in range(a):
        aux = pilas[b - 1].pop()
        pilas[c - 1].append(aux)
s = ""
for j in range(n):
    s += pilas[j][-1]
print(s.replace("[","").replace("]",""))
archivo.close()