import itertools

digits = ["0","1","2","3","4","5","6","7","8","9"]
list = itertools.permutations(digits)
s = 0
primes = [0,2,3,5,7,11,13,17]
#list = [("1","4","0","6","3","5","7","2","8","9")]
#brute force method
for i in list:
    if i[0] == "0":
        continue
    b = ""
    for j in i:
        b+=str(j)
    flag = True
    for j in range(1,8):
        a = ""+i[j]+i[j+1]+i[j+2]
        if int(a)%primes[j]:
            flag = False 
            break
    if flag:
        print(b," pass")
        s+=int(b)
    else:
        print(b," fail")
print(s)
