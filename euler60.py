import numpy as np
from collections import defaultdict
from itertools import combinations
from primes import *
from math import ceil

def sort(a,b):
    return (a,b) if a<b else (b,a)


def solve(target):
    pset = frozenset(primes)
    edges = set()

    def isprime(pstr):
        p = int(pstr)
        if p < primes[-1]:
            return p in pset
        else:
            lim = ceil(p ** 0.5)
            for x in primes:
                if p % x != 0:
                    return False
                if x > lim:
                    return True
            print("Ran out of primes ya fool!")
            exit()
    #2-cliques,3-cliques...k-cliques
    k_cliques = [[] for x in range(target-1)]
    connected = defaultdict(int)
    edges = defaultdict(bool)

    for idx,b in enumerate(primes):
        x = str(b)

        vertices = set()
        for a in primes[:idx]:
            y = str(a)

            if isprime(x+y) and isprime(y+x):
                connected[a] += 1
                connected[b] += 1
                edges[(a,b)] = True

                if connected[a] >= target-1 or connected[b] >= target-1:
                    edges[(b,a)] = True
                    clique_new = []

                    for k_clique in k_cliques:
                        k_clique += clique_new
                        clique_new = []
                        for clique in k_clique:
                            a_in = a in clique
                            b_in = b in clique
                            if a_in and b_in:
                                continue
                            if a_in and all(edges[sort(x,b)] for x in clique):
                                new_clique = tuple(list(clique)+[b])
                                clique_new.append(new_clique)
                            elif b_in and all(edges[sort(x,a)] for x in clique):
                                new_clique = tuple(list(clique)+[a])
                                clique_new.append(new_clique)
                    k_cliques[0].append((a,b))


                    if k_cliques[-1]:
                        x = k_cliques[-1].pop()
                        print(x,sum(x))
                        #return sum(x)
                        exit()
print(solve(5))

