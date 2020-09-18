from primes import *
import numpy as np

bound = 1000000


#too slow
def sub_vertical(bound):
    count = (bound-1)*(bound-1+1)/2
    print(count)
    for x in range(2,bound):
        if x in primes:
            z = (bound - x) // (x)
        else:
            z = 0
            pfs = pfactors(x)
            for n in range(x+1,bound+1):
                if any(n%pf==0 for pf in pfs):
                    z+=1
        count -= z
    return count

#oeis a002088
#still slow
def try2(n):
    n = n+1
    a = [1]
    a = np.empty(n+1,dtype=np.int32)
    for i in range(1,n):
        a[i] = i*(i+3)/2 - a[i//np.arange(2,i+1)].sum()
        print(i)

    return a[i]-2


def seive(n):
    n+=1
    phis = np.arange(n)
    for i in primes:
        k = i
        while k < n:
            phis[k] *= (1 - 1/i)
            k += i
    return np.sum(phis)-1

#phi sequence: 1, 1, 2, 2, 4, 2, 6, 4, 6, 4, 10,
print(seive(1000000))

