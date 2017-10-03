


a = 1
b = 2
c = 5
d = 0
count = 0
for a in range(2,1000000):
    d = c
    c = 2*c+b
    a = b
    b = d

    q = d + c
    if len(str(q))>len(str(c)):
        count+=1
    
print(count)
    
