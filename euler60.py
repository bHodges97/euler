import numpy as np
from collections import defaultdict
from itertools import combinations
from primes import *
from math import ceil



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
    k_cliques = [set() for x in range(target-1)]
    edges = defaultdict(bool)
    connected = defaultdict(int)
    graph = set()
    verts = set()

    for idx,b in enumerate(primes):
        x = str(b)
        new_edges = set()

        vertices = set()
        for a in primes[:idx]:
            y = str(a)

            if isprime(x+y) and isprime(y+x):
                connected[a] += 1
                connected[b] += 1

                if connected[a] >= target-1 and connected[b] >= target-1:
                    edges[(a,b)] = True
                    edges[(b,a)] = True
                    new_edges.add((a,b))

                    vertices.add(a)
                    vertices.add(b)



        if new_edges:
            k_cliques[0] |= new_edges
                #k-1 ... 0

            clique_new = set()
            for k_clique in k_cliques:
                k_clique |= clique_new
                clique_new = set()

                for clique in k_clique:
                    for v in vertices:
                        if all(edges[(x,v)] for x in clique):
                            new_clique = tuple(sorted(list(clique)+[v]))
                            clique_new.add(new_clique)

            if k_cliques[-1]:
                x = k_cliques[-1].pop()
                print(x,sum(x))
                #return sum(x)
                exit()
print(solve(4))

