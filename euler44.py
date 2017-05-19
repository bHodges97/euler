
a = []
sol = []

#this bound is just a guess \-.-/
for i in range(0,5000):
    a.append(int(i*(3*i-1)/2))

for j in range(2,len(a)):
    for i in range(1,j):
        if a[j]-a[i] in a and a[j]+a[i] in a:
            print(a[j],a[i],a[j]-a[i])
            sol.append(a[j]-a[i])

print(min(sol))

