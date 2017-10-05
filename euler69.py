import euler
from euler import *

n =  1000000
primes = primesUpTo(n)

def nover(phi):
    noverphi = phi[:]
    for i in range(1,n):
        noverphi[i] = (i)/phi[i]
    print(noverphi.index(max(noverphi)),",",max(noverphi))


#prime factorisation brute force
def solutionA():
    noverphi = [-1] * n
    for i in range(1,len(noverphi)):
        f = primeFactor(i)
        p = 1
        for fact in f:
            p*=1-1/fact
        noverphi[i]=1/p
        if i % 10000 == 0:
            print(i/n,"% done");
   

def solutionB():
    phi = [-1] * n
    done = [False] * n
    for p in primes:
        pk = p
        k = 1
        while pk < n:
            phi[pk]=pk*(1-1/p)
            done[pk]=True
            k+=1
            pk*=p
    print("Primes done!")
 
    for i in range(1,n):
        if phi[i] == -1 or not done[i]:
            continue
        for j in range(i+1,n):
            if not done[j]:
                continue
            if i*j >= n:
                break
            if phi[j] != -1 and not done[i*j]:
                phi[i*j] = phi[i]*phi[j]
    print("Primes x1!")
    for i in range(2,n):
        if phi[i]!=-1:
            continue
        phi[i]=phifunction(i)
        if i % 1000 == 0:
            print(i)
    print("clean up done")
    return phi

def product(a):
    b = 1
    for i in a:
        b*=i
    return b
def sproduct(a):
    b = 1
    for i in a:
        b*=(1-1/i)
    return b

def solC():

    counter = 0
    phi = [-1] * (n)
    psqrd = [-1] * (n)
    phi[2] = 1
    psqrda = []
    for i in primes:
        psqrda.append([])
    
    for p in primes:
        pk = p
        k = 1
        while pk < n:
            phi[pk]=int(pk*(1-1/p))
            psqrd[pk]=p
            #psqrda[primes.index(p)].append(pk)
            k+=1
            pk*=p
            counter+=1

    print(counter/n*100,"% done")
    for i in range(1,n):
        if psqrd[i] == -1: 
            continue
        for coprime in range(i+1,n):
            if phi[coprime] == -1 or psqrd[coprime] == -1:
                continue
            if psqrd[i] == psqrd[coprime]:
                continue
            if i * coprime >= n:
                break
            if phi[i] != -1 and phi[i*coprime] == -1 and coprime % i != 0:
                phi[i*coprime] = phi[i]*phi[coprime]
                counter+=1
    
    print(counter/n*100,"% done")
    
    # for i in psqrda[0]:
    #    while psqrd




    print(counter/n*100,"% done")
    missed = 0
    for i in range(2,n):
        if phi[i] == -1:
            phi[i] = euler.phi(i,primes)
            missed+=1
            counter+=1
        if i%10000 == 0:
            print(counter/n*100,"% done")
    print("Amount missed",missed)
    return phi

nover(solC())

