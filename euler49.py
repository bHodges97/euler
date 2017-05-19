file = open("primes.txt","r");
primes = file.read().split(",");
primes = [int(x) for x in primes if 1000 < int(x) < 10000] 

for ii in range(0,len(primes)):
    i = primes[ii]
    for jj in range(ii+1,len(primes)):
        j = primes[jj]
        k = 2*j-i
        if k in primes:
            if sorted(str(i)) == sorted(str(k)) == sorted(str(j)):
                print("found",i,j,k)
                break
