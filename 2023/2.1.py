cnt = 1
ans = 0
while True:
    try:
        line = input().split(":")[1]
        flag = True
        for conj in line.split(";"):
            d = {
                "red": 0,
                "blue": 0,
                "green": 0
            }

            for el in conj.split(","):
                el = el.strip().split()
                d[el[1]] += int(el[0])
            
            flag = flag and (d["red"] <= 12 and d["green"] <= 13 and d["blue"] <= 14)


        if flag:
            ans += cnt
        cnt += 1
        
    except:
        break
print(ans)