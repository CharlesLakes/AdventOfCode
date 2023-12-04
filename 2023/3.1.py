def check(matriz,y,x1,x2):
    flag = False
    for i in range(x1 - 1,x2 + 2):
        flag = flag or matriz[y + 1][i] != '.'
    for i in range(x1 - 1,x2 + 2):
        flag = flag or matriz[y - 1][i] != '.'
    flag = flag or matriz[y][x2 + 1] != '.'
    flag = flag or matriz[y][x1 - 1] != '.'

    return flag

matriz = []
aux = 0
while True:
    try:
        line = input().replace("\r","")
        matriz.append("." +  line + ".")
        aux = max(aux,len(line) + 2)
    except:
        break
matriz = ["."*aux] + matriz + ["."*aux]
#print(matriz)
ans = 0

for i in range(1,len(matriz) - 1):
    x1 = 1
    flag = False
    acum = 0
    for j in range(1,len(matriz[i])):
        if matriz[i][j].isnumeric():
            if not flag:
                x1 = j
            acum = acum*10 + int(matriz[i][j])
            flag = True
        else:
            if flag and check(matriz,i,x1,j - 1):
                ans += acum
            acum = 0
            flag = False
print(ans)

