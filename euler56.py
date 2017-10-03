


m = 0
a = 0
b = 0

def total(a):
    s = 0
    for i in str(a):
        s+=int(i)
    return s

for i in range(1,100):
    for j in range(1,100):
        r = total(i**j) 
        if r >  m:
            m = r
            a = i
            b = j

print(m," ",a," ",b," ")
