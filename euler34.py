#notes
#https://oeis.org/A068652 <-list of circular primes
#2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97 
#this solution takes roughly 1 min :(.

def solve():
    file = open("testfile.txt","r")
    primes  = [int(x) for x in file.read().split(',')]
    file.close()
    r = primes[:]
   # r = [x for x in r if x < 100]
    rotations = []
    total = 0
    for i in r:
        if i in rotations:
            continue
        string = str(i)
        flag = True
        temp = []
        for digit in range(0,len(string)):
            string = string[1:]+string[:1]
            integer = int(string)
            if integer not in primes:
                flag = False;
                break
            elif flag and integer not in rotations and integer not in temp:
                temp.append(integer)
        if flag:
            total+=len(temp)
            rotations.extend(temp)
            print(total," ",i)
    return len(rotations);
print(solve())
	    
