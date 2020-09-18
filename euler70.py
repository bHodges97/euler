from primes import *
import numpy as np

#thoughts: phi(prime) = 1 -> prime/1 no minimum likely
#phi n = n * sigma(1-1/p)
#the sum will have to turn n in to a permutation?


def seive(n):
    phis = np.arange(n,dtype=float)
    for i in primes:
        for k in range(i,n,i):
            phis[k] *= (1 - 1/i)
    return phis.astype(int)

#test =[0, 1, 1, 2, 2, 4, 2, 6, 4, 6, 4, 10, 4, 12, 6, 8, 8, 16, 6, 18, 8, 12, 10, 22, 8, 20, 12, 18, 12, 28, 8, 30, 16, 20, 16, 24, 12, 36, 18, 24, 16, 40, 12, 42, 20, 24, 22, 46, 16, 42, 20, 32, 24, 52, 18, 40, 24, 36, 28, 58, 16, 60, 30, 36, 32, 48, 20, 66, 32, 44]
#phis = seive(len(test))
#print(phis==test)
phis = seive(10**7)
print("generation done")


maxi = 100000000
for i in range(100,10**7):
    if sorted(str(i)) == sorted(str(phis[i])):
        ratio = i / phis[i]
        if ratio < maxi:
            maxi = ratio
            solution = i,phis[i]
print(solution)
