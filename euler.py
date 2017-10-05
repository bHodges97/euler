



def primesUpTo(upper):
    isPrime = list(range(upper))
    for p in range(2,int(upper**0.5)+1):
        if isPrime[p]:
            for multiple in range(p**2,upper,p):
                isPrime[multiple] = False
    return [x for x in isPrime[2:] if x]

def isPrime(n):
    return True

def divisors(n):
    c = 0
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            if i == n**0.5:
                c+=1
            else:
                c+=2
    return c

def primeFactor(n,primes):
    i = 0
    l = []
    while n != 1:
        if n%primes[i] == 0:
            n/=primes[i]
            l.append(primes[i])
        else:
            i+=1
    return l

def phi(n,primes):
    f = set(primeFactor(n,primes))
    p = 1
    for fact in f:
        p*=1-1/fact
    return int(p*n)


