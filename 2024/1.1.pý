l = []
r = []

while True:
    try:
        line = input().strip().split()
        l.append(int(line[0]))
        r.append(int(line[1]))
    except:
        break

l.sort()
r.sort()
ans = 0
for i in range(len(l)):
    ans += abs(l[i] - r[i])
print(ans)
