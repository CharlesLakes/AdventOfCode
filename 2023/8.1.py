moves = input().replace("\r","")
g = {}
while True:
    try:
        line = input().replace("\r","").split("=")
        left = line[0].strip()
        right = line[1].replace("(","").replace(")","").strip().split(",")
        g[left] = {"L":right[0].strip(),"R":right[1].strip()} 
    except:
        break
cnt = 0
current = "AAA"
while current != "ZZZ":
    pos = cnt % len(moves)
    current = g[current][moves[pos]]
    cnt += 1
print(cnt)