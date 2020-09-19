#lists of cubes by number of digits
lists = [[]]*100

for i in range(10,10000):
    cubed = i**3
    lists[len(str(cubed))].append(cubed)

for l in lists:
    #use a sorted str to check if its permutation
    l2 = [sorted(str(x)) for x in l]
    for idx,x in enumerate(l2):
        count = 0
        for x1 in l2[idx:]:
            if x1 == x:
                count+=1
            if count == 5:
                print(l[idx])
                exit()
