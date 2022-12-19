archivo = open("input.txt")

data = archivo.read().split("\n\n")
data = list(map(lambda a: a.strip().split("\n"),data))

valores = [0 for _ in range(len(data))]
for n,elfo in enumerate(data):
    for valor in elfo:
        valores[n] += int(valor)

valores.sort()
print(sum(valores[-3:]))
archivo.close()