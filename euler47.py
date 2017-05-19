 
file = open("primes.txt","r")
primes  = [int(x) for x in file.read().split(',')]
file.close()

def pfactors(n,l=[]):
    for i in primes:
         if n%i==0:
             l.append(i)
             a = n/i
             if a == 1:
                 return l
             else:   
                 return pfactors(a,l)  
l1 = 0
l2 = 0
l3 = 0
l4 = 0
for i in range(646, 199999900):
    l1 = l2
    l2 = l3
    l3 = l4
    fact = set(pfactors(i,[]))
    l4 = len(fact)
    if l1 == l2 == l3 == l4 == 4:
        print(i-3)
        break


