file = open("primes.txt","r")
primes = file.read().split(",")
primes = [int(x) for x in primes]


a = 2
primecount = 0
total = 1
c = 1

def isPrime(prime):
    i = 2
    for i in primes:
        if i == prime:
            return True
        if prime % i == 0:
            return False
    while i < prime**0.5:
        i+=2
        if prime % i == 0:
            return False
    return True
       
for k in range(100000):

    for i in range(4):
        total+=1
        c+=a
        if isPrime(c):
            primecount+=1
        
    a+=2
    print("Length: ", 2 * (k + 1) + 1 , " | Primes/Total: ", primecount,"/",total, " | Ratio: ", primecount/total)
    if primecount/total < 0.1:
        break

