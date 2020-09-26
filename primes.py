from math import gcd,prod

with open("primes.txt","r") as f:
    primes  = [int(x) for x in f.read().split(',')]

def eratosthenes_sieve(n):
    out = set(range(2,n))
    for i in range(2,n):
        if not i in out:
            continue
        for j in range(i+i,n,i):
            out.discard(j)
    return out

def pfactorise(n, factors=None):
    if not factors:
        factors = []

    for i in primes:
        q,r = divmod(n,i)
        if r == 0:
            factors.append(i)
            if q == 1:
                return factors
            else:
                return pfactorise(q, factors)

def pfactors(n):
    factors = set()
    for i in primes:
        if i > n:
            break
        elif not n % i:
            factors.add(i)

    return factors

def phi(n):
    return int(n * prod((1 - 1/p) for p in pfactors(n)))
    #x = 0
    #for i in range(1,n+1):
    #    if gcd(n,i) == 1:
    #        x += 1
    #return x

def farey(limit):
    pend = []
    n = 0
    d = N = D =1
    while True:
        mediant_d = d +D
        if mediant_d <= limit:
            mediant_n  = n + N
            pend.append((mediant_n, mediant_d, N, D))
            N = mediant_n
            D = mediant_d
        else:
            yield n,d
            if pend:
                n,d,N,D = pend.pop()
            else:
                break

if __name__ == "__main__":
    pass
    #primes = eratosthenes_sieve(10**7)
    #with open("primes.txt",'w') as f:
    #    f.write(",".join(map(str,sorted(primes))))




