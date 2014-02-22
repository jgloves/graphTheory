# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import networkx as nx

# <codecell>

import numpy as np

# <codecell>

from itertools import permutations

# <codecell>

def areIsomorphic(G, H):
    n = len(G.nodes())
    m = len(H.nodes())
    if n != m:
        return False
    if sorted(G.degree().values()) != sorted(H.degree().values()):
        return False
    else:
        a_g = nx.adjacency_matrix(G)
        vertex_perms = list(permutations(H.nodes(), m))
        for i in vertex_perms:
            a_h = nx.adjacency_matrix(H, i)
            if (a_h == a_g).all():
                #print(list(zip(G.nodes(), i)), "is an isomorphism") 
                return True
        return False
                                

# <codecell>

G = nx.Graph()

# <codecell>

G.add_nodes_from([1,2,3,4,5])
G.add_edges_from([(1,2), (2,3), (3,4), (4,5)])

# <codecell>

nx.draw(G)

# <codecell>

H = nx.Graph()
H.add_nodes_from(['a', 'd', 'e', 'b', 'c'])
H.add_edges_from([('a', 'd'), ('d', 'e'), ('e', 'b'), ('b', 'c')])
nx.draw(H)

# <codecell>

areIsomorphic(G,H)

# <codecell>

A = nx.Graph()
A.add_nodes_from([1, 2, 3, 4, 5])
A.add_edges_from([(1, 4), (1, 2), (1, 5), (2, 5), (2, 3), (3, 4), (3, 5)])
nx.draw(A)

# <codecell>

B = nx.Graph()
B.add_nodes_from(['a', 'b', 'c', 'd', 'e'])
B.add_edges_from([('a', 'b'), ('a', 'c'), ('a', 'e'), ('c', 'd'), ('d', 'e'), ('b', 'd'), ('c', 'e')])
nx.draw(B)

# <codecell>

areIsomorphic(A,B)

# <codecell>

C = nx.Graph([(1, 3), (2, 3), (3, 4), (3, 6), (5, 6), (6, 7), (7, 8), (6, 9), (9, 10)])
nx.draw(C)

# <codecell>

D = nx.Graph([('a', 'c'), ('b', 'c'), ('c', 'd'), ('c', 'e'), ('e', 'f'), ('f', 'h'), ('g', 'h'), ('h', 'j'), ('h', 'i')])
nx.draw(D)

# <codecell>

areIsomorphic(C, D)

# <codecell>

E = nx.Graph([(1, 2), (2, 3), (1, 5), (5, 3), (4, 5), (4, 3), (1, 4)])
nx.draw(E)

# <codecell>

F = nx.Graph([('a', 'e'), ('a', 'b'), ('b', 'e'), ('d', 'e'), ('c', 'd'), ('b', 'd'), ('b', 'c')])
nx.draw(F)

# <codecell>

areIsomorphic(E, F)

# <codecell>

I = nx.Graph([(1, 5), (1, 2), (2, 6), (3, 6), (3, 4), (5, 6), (4, 5), (1, 4), (2, 3)])
nx.draw(I)

# <codecell>

J = nx.Graph([('a', 'b'), ('a', 'e'), ('e', 'f'), ('b', 'f'), ('a', 'c'), ('b', 'c'), ('c', 'd'), ('d', 'e'), ('d', 'f')])
nx.draw(J)

# <codecell>

areIsomorphic(I, J)

# <codecell>

K = nx.Graph([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (1, 8), (1, 5), (2, 8), (3, 7), (4, 6)])
nx.draw(K)

# <codecell>

L = nx.Graph([('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e'), ('e', 'f'), ('f', 'g'), ('g', 'h'), ('a', 'h'), ('a', 'f'), ('b', 'e'), ('c', 'h'), ('d', 'g')])
nx.draw(L)

# <codecell>

areIsomorphic(K, L)

# <codecell>

M = nx.Graph([(1, 2), (2, 3), (3, 4), (1, 4), (5, 6), (6, 7), (7, 8), (5, 8), (4, 8), (3, 7)])
nx.draw(M)

# <codecell>

N = nx.Graph([(1, 2), (2, 4), (3, 4), (1, 3), (5, 6), (6, 8), (7, 8), (5, 7), (3, 5), (2, 8)])
nx.draw(N)

# <codecell>

areIsomorphic(M, N)

# <codecell>


