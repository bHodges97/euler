import math

i = 286
while True:
    a = i*(i+1)/2
    b = (math.sqrt(24*a+1)+1)/6
    c = (math.sqrt(8*a+1)+1)/4
    if c == int(c) and b == int(b):
        print(a)
        break
    i+=1
