archivo = open("input.txt")

dividers = [
    [[2]],
    [[6]]
]

data = archivo.read().strip().split("\n")
data = list(filter(lambda a: len(a) > 0,data))
data = list(map(eval,data))
data += dividers

def recur(left,right):
    print(left,right)    

    if type(left) == type(right) == list:
        i = 0
        while i < len(left) and i < len(right):
            if type(left[i]) == type(right[i]) == int:
                if left[i] < right[i]:
                    return 1
                if right[i] < left[i]:
                    return 0
            else:
                result = recur(left[i],right[i])
                if result == 1:
                    return 1
                if not result:
                    return result
            i += 1
        if len(right) < len(left):
            return 0
        if len(right) == len(left):
            return 2
        return 1

    if type(left) == int and type(right) == list:
        return recur([left],right)

    if type(right) == int and type(left) == list:
        return recur(left,[right])

    return False

for i in range(len(data)):
    for j in range(len(data) - i - 1):
        if not recur(data[j],data[j + 1]):
            aux = data[j]
            data[j] = data[j + 1]
            data[j + 1] = aux

a = data.index([[2]]) + 1
b = data.index([[6]]) + 1
print(a,b,a*b)


archivo.close()
