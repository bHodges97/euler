from math import factorial

skip = set()
lim = 1000000

def ssum(n):
    s = sum((factorial(int(x)) for x in str(n)))
    skip.add(s)
    return s


cmap = {i:ssum(i) for i in range(lim)}

total = 0
for i in range(lim):
    if i in skip:
        continue
    chainlen = 0
    current = i
    past = set()
    while current not in past:
        if current not in cmap:
            cmap[current] = ssum(current)
        past.add(current)
        current = cmap[current]
        chainlen+=1

    if chainlen == 60:
        total += 1
print(total)

