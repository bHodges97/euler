from primes import pfactorise

l1 = 0
l2 = 0
l3 = 0
l4 = 0
for i in range(646, 199999900):
    l1 = l2
    l2 = l3
    l3 = l4
    fact = set(pfactorise(i,[]))
    l4 = len(fact)
    if l1 == l2 == l3 == l4 == 4:
        print(i-3)
        break


