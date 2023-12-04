def check(matriz,values,y,x1,x2,acum):
    for i in range(x1 - 1,x2 + 2):
        if matriz[y + 1][i] == '*':
            if not values[y + 1][i][0]:
                values[y + 1][i][0] = 1
            values[y + 1][i][0] *= acum
            values[y + 1][i][1] += 1
    for i in range(x1 - 1,x2 + 2):
        if matriz[y - 1][i] == '*':
            if not values[y - 1][i][0]:
                values[y - 1][i][0] = 1
            values[y - 1][i][0] *= acum
            values[y - 1][i][1] += 1
    if matriz[y][x2 + 1] == '*':
        if not values[y][x2 + 1][0]:
            values[y][x2 + 1][0] = 1
        values[y][x2 + 1][0] *= acum
        values[y][x2 + 1][1] += 1
    if matriz[y][x1 - 1] == '*':
        if not values[y][x1 - 1][0]:
            values[y][x1 - 1][0] = 1
        values[y][x1 - 1][0] *= acum
        values[y][x1 - 1][1] += 1
    return flag

matriz = []
values = []
aux = 0
while True:
    try:
        line = input().replace("\r","")
        matriz.append("." +  line + ".")
        aux = max(aux,len(line) + 2)
        values.append([[0,0] for _ in range(len(line) + 2)])
    except:
        break
matriz = ["."*aux] + matriz + ["."*aux]
values = [[[0,0] for _ in range(aux)]] + values + [[[0,0] for _ in range(aux)]]
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
            if flag and check(matriz,values,i,x1,j - 1,acum):
                ans += acum
            acum = 0
            flag = False
ans =0
for line in values:
    for e in line:
        if e[1] != 2:
            continue
        ans += e[0]

print(ans)

