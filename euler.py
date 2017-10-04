



def primesUpTo(upper):
    isPrime = list(range(upper))
    for p in range(2,int(upper**0.5)+1):
        if isPrime[p]:
            for multiple in range(p**2,upper,p):
                isPrime[multiple] = False
    return [x for x in isPrime[2:] if x]

def isPrime(n):
    return True

def primeFactor(n):
    i = 0
    l = []
    while n != 1:
        if n%primes[i] == 0:
            n/=primes[i]
            l.append(primes[i])
        else:
            i+=1
        return l

def phi(n):
    f = primeFactor(n)
    p = 1
    for fact in f:
        p*=1-1/fact
    return p*a
