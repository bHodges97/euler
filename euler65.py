#approximate e

from math import e,gcd
from fractions import Fraction


def twok(i):
    if (i+1) % 3 == 0:
        return (i+1) // 3 * 2
    else:
        return 1

x = 0
for i in range(99,0,-1):
    x = Fraction(1,(twok(i) + x))

solution =2+x
print(solution,e)
print(sum(int(x) for x in str(solution.numerator)))




