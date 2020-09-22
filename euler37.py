#as per usual the answer is on wikipedia and the and eois
#https://oeis.org/A020994
from time import time


def solve():
    with open("primes.txt","r") as f:
        primes  = [int(x) for x in f.read().split(',')]

    count = 0
    ans = 0
    left_set = {'2','3','5','7'}
    right_set = {'2','3','5','7'}

    while count != 11:
        left_tmp = set()
        right_tmp = set()

        #odds and primes
        for i in ['1','2','3','5','7','9']:
            i = str(i)
            for x in left_set:
                left = i+x
                if int(left) in primes:
                    left_tmp.add(left)
                    #print(left)

        #right sight cannot end with 2 or 5
        for i in ['1','3','7','9']:
            for x in right_set:
                right = x+i
                if int(right) in primes:
                    right_tmp.add(right)
        left_set = left_tmp
        right_set = right_tmp

        both_set = left_set & right_set
        if both_set:
            print(both_set)
        count+=len(both_set)
        ans+=sum(int(x) for x in both_set)
        #print(count)
    return ans

t = time()
print("solution:",solve())
print("time:",time()-t)
