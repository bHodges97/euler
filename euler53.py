import math

def ncr(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

a=0
for n in range(1,101):
    for r in range(1,n):
        j = ncr(n,r)
        if j > 1000000:
            a+=1

print(a)
