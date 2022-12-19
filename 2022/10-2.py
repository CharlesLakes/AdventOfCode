archivo = open("input.txt")

data = archivo.read().split("\n")

x = 1
c = 1
screen = [[False for _ in range(40)] for _ in range(6)]
result = 0
for linea in data:
    
    temp = linea.split(" ")
    
    if len(temp) == 2:
        a = int(temp[1])
        for _ in range(2):
            if x <= ((c - 1) % len(screen[0])) + 1 < x + 3:
                #print(c)
                #print((c - 1) // len(screen[0]),(c - 1) % len(screen[0]))
                screen[(c - 1) // len(screen[0])][(c - 1) % len(screen[0])] = True
            c += 1
            
        x += a
    else:
        if x <= ((c - 1) % len(screen[0])) + 1 < x + 3:
            #print(c)
            #print((c - 1) // len(screen[0]),(c - 1) % len(screen[0]))
            screen[(c - 1) // len(screen[0])][(c - 1) % len(screen[0])] = True
        c += 1
        
            
for linea in screen:
    for x in linea:
        if x:
            print("#",end="")
        else:
            print(".",end="")
    print()

archivo.close()