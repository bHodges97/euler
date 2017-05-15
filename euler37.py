def check(a):
    if len(a)>9:
        return False
    for i in range(1,9):
        if i not in a:
            return False
    if len(a)==9:
        return 7
    return True

largest = 0
for i in range(1,987654321):
    totes = ""
    for j in range (1,10):
        totes+=str(i*j)
        j = check(totes)
        if j==7:
            a = int(totes)
            largest =  a if a > largest else largest
        elif not check(totes):
            break

print(largest)
