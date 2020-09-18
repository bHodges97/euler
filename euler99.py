with open("p099_base_exp.txt",'r') as f:
    lines = f.readlines()
    pairs = [x.strip().split(",") for x in lines]
    pairs = [(int(x),int(y)) for x,y in pairs]


def lessthan(a,b):
    base1,exp1 = a
    base2,exp2 = b

    smallexp = min(exp1,exp2)
    base1 = base1**(exp1/smallexp)
    base2 = base2**(exp2/smallexp)

    return base1 < base2

#test
a = (2,11)
b = (3,7)
print(lessthan(pairs[0],pairs[1]))

best = pairs[0]
lineno = 0

for idx,x in enumerate(pairs):
    if lessthan(best,x):
        best = x
        lineno = idx
#0 does count as line
print(best,lineno+1)
