def primes(upTo):
     isPrime = list(range(upTo))
     for p in range(2,int(upTo**0.5)+1): #p: 2,3,4,...,sqrt(N)
         if isPrime[p]:
             for multiple in range(p**2,upTo,p): #mult: p^2, p^2+p, p^2+2p, ..., N
                 isPrime[multiple] = False
     return [x for x in isPrime[2:] if x]

def solve(n):
    p = primes(n)
    a = [x for x in range(2,n+1) if x not in p and x % 2]
    for i in a:
        flag = True
        for j in p:
            if j >= i:
                break
            k = ((i-j)/2)**0.5
            if int(k) == k:
                flag = False
                break
        if flag:
            return(i)
            


print(solve(10**4))
