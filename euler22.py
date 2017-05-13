file = open("p022_names.txt")
data = file.read().replace("\"","").split(",")
data.sort()
sum = 0;
for index, a in enumerate(data):
    t = 0
    for c in a:
        t+= ord(c)-ord('A')+1
    sum+=(1+index)*t
print(sum)

