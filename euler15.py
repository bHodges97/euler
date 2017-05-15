def recursive(a,b):
    if a == 0 or b == 0:
        return 1;
    else:
        return recursive(a-1,b)+recursive(a,b-1)


# nCr 40,20  --> (2n!)/2(n!)
#137846528820
def flood(size):
    size+=1
    m = size*[size*[1]]
    for a in range(1,size):
        for b in range (1,size):
            m[a][b]=m[a-1][b]+m[a][b-1]
    return m[size-1][size-1]
    
print(flood(20))
print(recursive(3,3))
