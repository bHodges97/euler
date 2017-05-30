

a = 0;
for i in range (10000):
    j = 0;
    k=i+int(str(i)[::-1])
    while k!=int(str(k)[::-1]):
        k=k+int(str(k)[::-1]) 
        if j > 50:
            a+=1
            break
        j+=1
print(a)
