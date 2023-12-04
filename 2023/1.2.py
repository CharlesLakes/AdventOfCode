numbers = ["one", "two", "three","four","five","six","seven","eight","nine"]

for i in range(len(numbers)):
    r = numbers[i][::-1]
    numbers[i] = [numbers[i],r]

total = 0
while True:
    try:
        s = input()
        sr = s[::-1]
        last = float("inf")
        first = float("inf")
        vl = vf = 0
        cnt = 1
        for n,nr in numbers:
            if n in s:
                pos = s.find(n)
                if pos < first:
                    first = pos
                    vf = cnt
            if nr in sr:
                pos = sr.find(nr)
                if pos < last:
                    last = pos
                    vl = cnt
            if str(cnt) in s:
                pos = s.find(str(cnt))
                if pos < first:
                    first = pos
                    vf = cnt
            if str(cnt) in sr:
                pos = sr.find(str(cnt))
                if pos < last:
                    last = pos
                    vl = cnt
            cnt += 1
        total += vf*10 + vl
                
    except:
        break

print(total)