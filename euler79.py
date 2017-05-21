file = open("p079_keylog.txt","r")
text = file.read().split("\n")[:-1]


password=""
while text:
    text1 = [[x,0] for x in [x[0] for x in text]]
    text2 = [x[1:] for x in text]
    new = set()
    for a in text1:
        for b in text2:
            a[1]+=b.count(a[0])
        if a[1] == 0:
            new.add(a[0])
            a[0] = ''
    for a in new:
        password+=a

    text = [text1[x][0]+text2[x] for x in range(len(text1))]
    text = list(filter(None,text))   
    
print(password)
