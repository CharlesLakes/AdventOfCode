def check(values):
    isIncresing = True
    isDecresing = True
    atMostThree = True
    
    for i in range(1,len(values)):
        isIncresing = isIncresing and (values[i - 1] < values[i])
        isDecresing = isDecresing and (values[i - 1] > values[i])
        atMostThree = atMostThree  and (abs(values[i - 1] - values[i]) <= 3)

    if not isIncresing and not isDecresing:
        return False
    return atMostThree



ans = 0

while True:
    try:
        values = input().strip().split()
        values = list(map(int,values))
        if check(values):
            ans += 1
        else:
            for i in range(len(values)):
                if check(values[:i] + values[i+1:]):
                    ans += 1
                    break
    except:
        break

print(ans)
