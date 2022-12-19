archivo = open("input.txt")

data = archivo.read()
memo = data[:13]
for i in range(13,len(data)):
    temp = memo + data[i]
    print(temp)
    status = True
    for j in range(len(temp)):
        if temp[j] in (temp[:j] + temp[j + 1:]):
            status = False
            break
    print(status)
    if not status:
        memo = memo[1:] + data[i]
    else:
        break

print(i + 1)
archivo.close()