def check(current):
    flag = True
    for e in current:
        flag = flag and e[-1] == "Z"
    return flag

moves = input().replace("\r","")
g = {}
current = []
while True:
    try:
        line = input().replace("\r","").split("=")
        left = line[0].strip()
        right = line[1].replace("(","").replace(")","").strip().split(",")
        if left[-1] == 'A':
            current.append(left)
        g[left] = {"L":right[0].strip(),"R":right[1].strip()} 
    except:
        break

print(current)
ends = ['QGZ','JVZ','ZZZ','VQZ','JNZ','MGZ']
counts = [[] for _ in range(len(current))]


cnt = 0
while not check(current):
    pos = cnt % len(moves)
    flag = True
    for i in range(len(current)):
        if current[i] == ends[i] and len(counts[i]) < 3:
            print(current[i],pos)
            counts[i].append(cnt)
        flag = flag and len(counts[i]) == 3
        current[i] = g[current[i]][moves[pos]]
    if flag:
        break
    cnt += 1

print(counts)
ma = 0
for e in counts:
    print(e[1] - e[0],end=",")
    ma = max(ma,e[0])
print()
for e in counts:
    print((e[1] - ma) % (e[1] - e[0]),end=",")
print()
print(ma + 16342438686552)