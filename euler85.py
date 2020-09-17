target = 2000000

#for 1xn:
def count(width,height):
    total = 0
    w1 = width+1
    h1 = height+1
    for x in range(1,w1):
        for y in range(1,h1):
            total += (w1-x) * (h1-y)



    return total
#test
#print(count(2,3))

closest = ()
best = target
for x in range(100):
    for y in range(100):
        new = abs(count(x,y) - target)
        if  new < best:
            best = new
            closest = [x,y,count(x,y)]
print(closest,closest[0]*closest[1])
print(best)
