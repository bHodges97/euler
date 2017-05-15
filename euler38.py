digs = ["1","2","3","4","5","6","7","8","9"]

def check(a):
    for i in digs:
        if not i in a:
            return False
    return True

largest = 0
for i in range(1,1000000):
    totes = ""
    j = 1;
    while(len(totes)<9):
        totes+=str(i*j)
        j+=1
    if(len(totes)!=9):continue
    if check(totes):
        a = int(totes)
        largest =  a if a > largest else largest

print(largest)
