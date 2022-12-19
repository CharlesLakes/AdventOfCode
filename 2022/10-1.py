archivo = open("input.txt")

data = archivo.read().split("\n")

x = 1
c = 1
aux = [20, 60, 100, 140, 180, 220]
result = 0
pos = 0
for linea in data:
    
    temp = linea.split(" ")

    if len(temp) == 2:
        a = int(temp[1])
        for _ in range(2):
            if pos == len(aux):
                break
            if c == aux[pos]:
                result += aux[pos]*x
                pos += 1
            c += 1
            
        x += a
    else:
        if pos == len(aux):
                break
        if c == aux[pos]:
            result += aux[pos]*x
            pos += 1
        c += 1
        
            

    print(result)

archivo.close()