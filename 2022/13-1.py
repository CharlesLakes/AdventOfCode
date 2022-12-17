archivo = open("input.txt")

data = archivo.read().strip().split("\n\n")
data = list(map(lambda a: a.split("\n"),data))
data = [list(map(eval,x)) for x in data]


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

i = 1
suma = 0
for left,right in data:
    if recur(left,right):
        suma += i
    i += 1
print(suma)
archivo.close()
