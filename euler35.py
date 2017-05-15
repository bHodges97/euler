sum = 0;
for i in range(1,1000000):
    string = str(i)
    flag = False
    for j in range (0,int(len(string)/2)):
        if string[j]!=string[-j-1]:
            flag = True
            break
    if flag:
        continue
    string = bin(i)[2:]
    for j in range (0,int(len(string)/2)):
        if string[j]!=string[-j-1]:
            flag = True
            break
    if not flag:
        sum+=i
print(sum)
