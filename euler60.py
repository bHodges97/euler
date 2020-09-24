import numpy as np
from collections import defaultdict
from itertools import combinations
from primes import *
from math import ceil

target = 4


def in_graph(a,b,graph):
    return ((a,b) if a < b else (b,a)) in graph

def k_cliques(graph):
    print("hi")
    vertices = set()
    degrees = defaultdict(int)

    for v in graph:
        for i in v:
            degrees[i]+=1

    vertices = {i for i,j in degrees.items() if j>target}

    cliques_v = {(i,j) for i,j in graph}
    cliques = [[tuple(x)] for x in cliques_v]
    k = 2

    while cliques:
        yield k, cliques_v

        cliques_1 = set()
        for clique in cliques_v:
            for v in vertices:
                if all(in_graph(v,x,graph) for x in clique):
                    new_clique = tuple(sorted(list(clique)+[v]))
                    cliques_1.add(new_clique)

        cliques_v = cliques_1
        k += 1

def solve():
    pset = frozenset(primes)
    edges = set()
    print(len(primes))

    def isprime(pstr):
        p = int(pstr)
        if pstr[0] == '0':
            return False
        elif p < primes[-1]:
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

    for x in primes:
        x = str(x)
        for j in range(1,len(x)):
            a,b = x[:j], x[j:]
            if a!=b and isprime(a) and isprime(b) and isprime(b+a):
                a,b = sorted([int(a),int(b)])
                edges.add((a,b))
    edges = frozenset(edges)
    print("edge gen ok",len(edges))

    for k,c in k_cliques(edges):
        print(k,"clique done")
        if k == target:
            c = ((sum(x),x) for x in c)
            c = sorted(c,key=lambda x:x[0])

            print(c[:4])
            break

        print("----")



solve()

