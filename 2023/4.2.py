ans = 0
counts = [1 for _ in range(300)]
i = 1
while True:
    try:
        r = input().split(":")[1].split("|")
        left = r[0].strip().split()
        right = r[1].strip().split()
        
        cnt = 0
        for e in right:
            if e in left:
                cnt += 1
        if cnt:
            for j in range(i + 1,i + cnt + 1):
                counts[j] += counts[i]
        ans += counts[i]
        i += 1
    except:
        break
print(ans)