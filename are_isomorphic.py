# -*- coding: utf-8 -*-
"""Functions that will determine whether two graphs are isomorphic.
   The graph isomorphism problem is a hard one. I will add more
   functions as I think of faster algorithms to use.
   
   Note: One (small) improvement to are_isomorphic() would be to 
   	let vertex_perms be only the list of vertex permutations 
   	of H for which the induced "degree sequence" preserves
   	that of the ordering of vertices in a_g.
"""

import networkx as nx

import numpy as np

from itertools import permutations

def are_isomorphic(G, H):
    """Check whether two graphs G and H are isomorphic.
    
    Note: This function is brute force and very slow.
    
    args:
        G: a networkx Graph
        H: a networkx Graph
    
    returns:
    	True if G and H are isomorphic.
    	False if G and H are not isomorphic.
    """
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

if __name__ == "__main__": 
	
	# some examples for testing 
	
	G = nx.Graph()
	
	G.add_nodes_from([1,2,3,4,5])
	G.add_edges_from([(1,2), (2,3), (3,4), (4,5)])
	
	nx.draw(G)
	
	H = nx.Graph()
	H.add_nodes_from(['a', 'd', 'e', 'b', 'c'])
	H.add_edges_from([('a', 'd'), ('d', 'e'), ('e', 'b'), ('b', 'c')])
	nx.draw(H)
	
	are_isomorphic(G,H) #True
	
	A = nx.Graph()
	A.add_nodes_from([1, 2, 3, 4, 5])
	A.add_edges_from([(1, 4), (1, 2), (1, 5), (2, 5), (2, 3), (3, 4), (3, 5)])
	nx.draw(A)
	
	B = nx.Graph()
	B.add_nodes_from(['a', 'b', 'c', 'd', 'e'])
	B.add_edges_from([('a', 'b'), ('a', 'c'), ('a', 'e'), ('c', 'd'), ('d', 'e'), ('b', 'd'), ('c', 'e')])
	nx.draw(B)
	
	are_isomorphic(A,B) #True
	
	C = nx.Graph([(1, 3), (2, 3), (3, 4), (3, 6), (5, 6), (6, 7), (7, 8), (6, 9), (9, 10)])
	nx.draw(C)
	
	D = nx.Graph([('a', 'c'), ('b', 'c'), ('c', 'd'), ('c', 'e'), ('e', 'f'), ('f', 'h'), ('g', 'h'), ('h', 'j'), ('h', 'i')])
	nx.draw(D)
	
	are_isomorphic(C, D) #False
	
	E = nx.Graph([(1, 2), (2, 3), (1, 5), (5, 3), (4, 5), (4, 3), (1, 4)])
	nx.draw(E)
	
	F = nx.Graph([('a', 'e'), ('a', 'b'), ('b', 'e'), ('d', 'e'), ('c', 'd'), ('b', 'd'), ('b', 'c')])
	nx.draw(F)
	
	are_isomorphic(E, F) #False
	
	I = nx.Graph([(1, 5), (1, 2), (2, 6), (3, 6), (3, 4), (5, 6), (4, 5), (1, 4), (2, 3)])
	nx.draw(I)
	
	J = nx.Graph([('a', 'b'), ('a', 'e'), ('e', 'f'), ('b', 'f'), ('a', 'c'), ('b', 'c'), ('c', 'd'), ('d', 'e'), ('d', 'f')])
	nx.draw(J)
	
	are_isomorphic(I, J) #True
	
	K = nx.Graph([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (1, 8), (1, 5), (2, 8), (3, 7), (4, 6)])
	nx.draw(K)
	
	L = nx.Graph([('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e'), ('e', 'f'), ('f', 'g'), ('g', 'h'), ('a', 'h'), ('a', 'f'), ('b', 'e'), ('c', 'h'), ('d', 'g')])
	nx.draw(L)
	
	are_isomorphic(K, L) #False
	
	M = nx.Graph([(1, 2), (2, 3), (3, 4), (1, 4), (5, 6), (6, 7), (7, 8), (5, 8), (4, 8), (3, 7)])
	nx.draw(M)
	
	N = nx.Graph([(1, 2), (2, 4), (3, 4), (1, 3), (5, 6), (6, 8), (7, 8), (5, 7), (3, 5), (2, 8)])
	nx.draw(N)
	
	are_isomorphic(M, N) #False
	

