

m = []
file = open("p082_matrix.txt","r")
n = list(file.read().split("\n"))[:-1]
for i in range(0,len(n)):
    m.append(n[i].split(","))
for a in range(0,len(m)):
    for b in range(0,len(m[0])):
        m[a][b]=int(m[a][b])
#test case 994
#m=[[131,673,234,103,18],[201,96,342,965,150],[630,830,746,422,111],[537,699,497,121,956],[805,732,524,37,331]]
v = [x[:] for x in m]

def flood(size):

    #work it out for first column
    for a in range(1,size):
        if m[a][0] > m[a-1][0]+v[a][0]:
            m[a][0] = m[a-1][0]+v[a][0]
    for a in reversed(range(0,size-1)):
        if m[a][0] > m[a+1][0]+v[a][0]:
            m[a][0] = m[a+1][0]+v[a][0]
    #rest
    for b in range(1,size):
        for a in range(0,size):
            m[a][b]+=m[a][b-1]
        for a in range(1,size):
            if m[a][b] > m[a-1][b]+v[a][b]:
                m[a][b] = m[a-1][b]+v[a][b]
        for a in reversed(range(0,size-1)):
            if m[a][b] > m[a+1][b]+v[a][b]:
                m[a][b] = m[a+1][b]+v[a][b]

    for a in range(0,len(m)):
        print(m[a])
    return min([x[-1] for x in m])

print(flood(len(m)))
