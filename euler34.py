import math

t = 0
for i in range(3,1000000):
    s = 0;
    for j in str(i):
        s+=math.factorial(ord(j)-ord("0"))
    if s == i:
        t+=s;
print(t)
