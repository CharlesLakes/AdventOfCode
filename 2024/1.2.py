l = []
r = {}

while True:
    try:
        line = input().strip().split()
        l.append(int(line[0]))
        if int(line[1]) not in r:
            r[int(line[1])] = 0
        r[int(line[1])] += 1 
    except:
        break

ans = 0
for i in range(len(l)):
    if l[i] not in r:
        continue
    ans += l[i]*r[l[i]]

print(ans)
