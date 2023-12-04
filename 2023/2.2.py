cnt = 1
ans = 0
while True:
    try:
        line = input().split(":")[1]
        flag = True
        dt = {
            "red": 0,
            "blue": 0,
            "green":0
        }
        for conj in line.split(";"):
            d = {
                "red": 0,
                "blue": 0,
                "green": 0
            }

            for el in conj.split(","):
                el = el.strip().split()
                d[el[1]] += int(el[0])
            
            for key in dt:
                dt[key] = max(dt[key],d[key])
        ans += dt["red"]*dt["blue"]*dt["green"]
        
    except:
        break
print(ans)