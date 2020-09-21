#notes
#https://oeis.org/A068652 <-list of circular primes
#2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97
#this solution takes roughly 1 min :(.
#on second thought ignoring ones that contain even numbers or 5
#made this take less than 1 second to solve :)

def solve():
   with open("primes.txt","r") as f:
      primes = [int(x) for x in f.read().split(",")]

   limit = 1000000
   primes = [x for x in primes if x < limit]
   circular = [0] * limit


   for idx,prime in enumerate(primes):
      if circular[prime]:
         continue
      if prime < 10:
         circular[prime] = 1
         continue

      prime_str = str(prime)
      digits = (int(x) for x in prime_str)
      is_circular = all(x%2!=0 and x!=5 for x in digits)

      rotations = [prime_str[x:] + prime_str[:x] for x in range(len(prime_str))]
      rotations = [int(x) for x in rotations if x[0] != '0']
      is_circular = is_circular and all(x in primes for x in rotations)

      for x in rotations:
         circular[x] = is_circular
   return sum(circular)
print(solve())

