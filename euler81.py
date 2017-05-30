

m = []
file = open("p081_matrix.txt","r")
n = list(file.read().split("\n"))[:-1]
for i in range(0,len(n)):
    m.append(n[i].split(","))
for a in range(0,len(m)):
    for b in range(0,len(m[0])):
        m[a][b]=int(m[a][b])

#m=[[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[537,699,497,121,956],[805,732,524,37,331]]

def flood(size):
    for a in range(1,size):
        m[a][0]+=m[a-1][0]
        m[0][a]+=m[0][a-1]
    for a in range(1,size):
        for b in range (1,size):
            m[a][b]=min([m[a][b]+m[a-1][b],m[a][b]+m[a][b-1]])
    return m[size-1][size-1]
for a in range(0,len(m)):
    print(m[a])
print(flood(80))
