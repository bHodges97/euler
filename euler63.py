

i = 2
count = 1
j = i
n = 1
while True:
    length = len(str(j))
    if length == n:
        count+=1
    elif length < n:
        if n == 2 and length != 1:
            print(count)
            break
        i+=1
        j=i
        n=1
        continue
    #text in base 10 so 10 onwards the length will never pass the power
    elif i >= 10:
        print(count)
        break
    j*=i
    n+=1

