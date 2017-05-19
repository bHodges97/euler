prod = 1;
digit = 0
counter = 0
targets = [1,10,100,1000,10000,100000,1000000]
for i in range(0,1000000):
    stri = str(i)
    leng = len(stri)
    if digit+leng>targets[counter]:
        prod*=int(stri[targets[counter]-digit])
        counter+=1
        if counter == len(targets):
            break
    digit+=leng

print(prod)

