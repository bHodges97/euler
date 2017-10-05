
j = 20

while True:
    j+=20
    b = True
    for i in range(19,2,-1):
        if j%i != 0:
            b = False
            break
    if b:
        print(j)
        break
