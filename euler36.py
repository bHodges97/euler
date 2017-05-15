#as per usual the answer is on wikipedia and the and eois
#https://oeis.org/A020994

def solve():
    file = open("primes.txt","r")
    primes  = [int(x) for x in file.read().split(',')]
    file.close()
    r = primes[4:]
    sum = 0
    for i in r:
        left = str(i)
        if '2' in left or '4' in left or '5' in left or '6' in left or '8' in left or '0' in left:
            continue
        right = left
        k = len(left)
        flag = False
        for j in range(0,k-1):
            left=left[1:]
            if int(left) not in primes:
                flag = True
                break
            right=right[:-1]
            if int(right) not in primes:
                flag = True
                break
        if not flag:
            sum+=i
    return sum;
print(solve())
	    
