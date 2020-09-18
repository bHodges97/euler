from math import gcd



lbound = 1/3
hbound = 1/2
dmax = 12000

#1/2 - 1/3 = 1/6 = 0.16666666666666666

#test bound 8

#dmax = 8
n,d = 1,3
count = 0
for dd in range(2,dmax + 1):
    for nn in range(dd//3,dd//2 + 1):
        if gcd(dd,nn) == 1 and nn/dd > lbound:
            count+=1
print(count-1)




