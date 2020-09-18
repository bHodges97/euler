target = 2000000

#for 1xn:
def count(width,height):
    total = width * (width + 1) *  height * (height + 1) / 4
    return total

print("test:",count(2,3))

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
