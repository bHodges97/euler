i = 10
f = False
while not f:
    i+=1
    f=True
    t = str(i)
    for j in range(2,7):
        p = i*j
        for k in str(p):
            if k not in t:
                f = False
                break
        if not f:
            break
print(i)
