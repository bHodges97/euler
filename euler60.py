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
        new_verts = set()
        for a in primes[:idx]:
            y = str(a)

            if isprime(x+y) and isprime(y+x):
                edges[(a,b)] = True
                connected[a]+=1
                connected[b]+=1

                if connected[a] >= target-1:
                    new_verts.add(a)
                    f = True

                if connected[b] >= target-1:
                    new_verts.add(b)
                    f = True

                graph.add((a,b))

        if new_verts:
            verts |= new_verts
            k_cliques_new = [set() for x in range(target-1)]
            graph_tmp = set()
            for a,b in graph:
                if a in verts and b in verts:
                    graph_tmp.add((a,b))
            graph -= graph_tmp
            k_cliques[0] |= graph_tmp


            for q in new_verts:
                #k-1 ... 0
                for i in range(len(k_cliques)-2,-1,-1):
                    for clique in k_cliques[i]:
                        if all(edges[(x,q)] for x in clique):
                            new_clique = tuple(list(clique)+[q])
                            k_cliques_new[i+1].add(new_clique)

                for cliques,cliques_new in zip(k_cliques,k_cliques_new):
                    cliques |= cliques_new

                if k_cliques[-1]:
                    x = k_cliques[-1].pop()
                    print(x,sum(x))
                    #return sum(x)
                    exit()
print(solve(5))

