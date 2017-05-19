
a = open("p042_words.txt","r")
b = a.read().split(",")
b = [x[1:-1] for x in b]

tri = []
for i in range(1,1000):
    tri.append(0.5*i*(i+1))


def val(n):
    return sum([ord(x)-64 for x in n])



s = 0
for n in b:
    if val(n) in tri:
        s+=1

print(s)
