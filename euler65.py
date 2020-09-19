#approximate e

from math import e,gcd

def twok(i):
    if (i+1) % 3 == 0:
        return (i+1) // 3 * 2
    else:
        return 1

target = 100
n,d = 1,twok(target-1)
for i in range(target-2,0,-1):
    n,d = d , d * twok(i) + n

n,d = 2*d+n,d
print(n/d,e)
print(sum(int(x) for x in str(n)))




