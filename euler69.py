f = open("primes.txt","r")
primes = f.read().split(",")
primes = [int(x) for x in primes]
n = 1000000

def generatePrimes(upper):
    isPrime = list(range(upper))
    for p in range(2,int(upper**0.5)+1):
        if isPrime[p]:
            for multiple in range(p**2,upper,p):
                isPrime[multiple] = False
    return [x for x in isPrime[2:] if x]

primes = generatePrimes(n)

def factorise_set(n):
    i = 0
    l = set()
    while n != 1:
        if n%primes[i] == 0:
            n/=primes[i]
            l.add(primes[i])
        else:
            i+=1
    return l

def solutionA():
    phi = [1] * n
    for i in range(2,n):
        print(i)
        factors = factorise(i)
        coprimes = range(i+1,n)
        for factor in factors:
            coprimes = [ x for x in coprimes if x%factor != 0]
        for coprime in coprimes:
            phi[coprime-1]+=1

    noverphi = phi[:]
    for i in range(1,n):
        noverphi[i] = (i+1)/phi[i]
    noverphi[-1]=0
    print(noverphi.index(max(noverphi))+1,",",max(noverphi))
  

def solutionB():
    phi = [-1] * n
    for p in primes:
        pk = p
        k = 1
        while pk < n:
            phi[pk]=pk*(1-1/p)
            k+=1
            pk*=p
    print("Primes done!")
 
    for i in range(1,n):
        if i != -1:
            for j in range(i+1,n):
                if i*j >= n:
                    break
                if j!= -1:
                    phi[i*j] = phi[i]*phi[j]

    print(n-len([x for x in phi if x != -1]))

    print("Not primes done!")
    noverphi = phi[:]
    for i in range(1,n):
        noverphi[i] = (i)/phi[i]
    print(noverphi.index(max(noverphi)),",",max(noverphi))


def factorise(n):
    i = 0
    l = []
    while n != 1:
        if n%primes[i] == 0:
            n/=primes[i]
            l.append(primes[i])
        else:
            i+=1
    return l

 
def solutionC():
    noverphi = [-1] * n
    for i in range(1,len(noverphi)):
        f = factorise(i)
        p = 1
        for fact in f:
            p*=1-1/fact
        noverphi[i]=1/p
        if i % 10000 == 0:
            print(i/n,"% done");
        



solutionC()
