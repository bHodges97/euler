

#stack overflow
def primes(upTo):
    isPrime = list(range(upTo))
    for p in range(2,int(upTo**0.5)+1): #p: 2,3,4,...,sqrt(N)
        if isPrime[p]:
            for multiple in range(p**2,upTo,p): #mult: p^2, p^2+p, p^2+2p, ..., N
                isPrime[multiple] = False
    return [x for x in isPrime[2:] if x]

def lpal(n):
    p = reversed(primes(n))
    for a in p:
        b = str(a)
        l = len(b)
        flag = True
        for i in range(1,l+1):
            if str(i) not in b:
                flag = False
                break
        if flag:
            return a
    return 0


print(lpal(10**7))
#print(sieve(10**7))
