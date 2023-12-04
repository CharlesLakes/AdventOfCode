ans = 0
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
            ans += 2**(cnt - 1)
    except:
        break
print(ans)