import numpy as np
import networkx as nx

def hardy_cross(G, n, init_guess=None):
    cycles = nx.cycle_basis(G)
    cycles = np.array([[tuple([cycles[j][i], cycles[j][i+1]]) if (i < len(cycles[j])-1) else tuple([cycles[j][i], cycles[j][0]]) for i in range(len(cycles[j]))] for j in range(len(cycles))])

    L = [G.node[i]['demand'] for i in G.node.keys()]
    edges = np.array(G.edges())
    edge_idx = np.full((len(G), len(G)), 9999, dtype=int)
    edge_idx[edges[:,0], edges[:,1]] = np.arange(len(G.edges()))
    edge_idx[edges[:,1], edges[:,0]] = np.arange(len(G.edges()))
    
    edge_dir = np.zeros((len(G), len(G)), dtype=int)
    edge_dir[edges[:,0], edges[:,1]] = 1
    edge_dir[edges[:,1], edges[:,0]] = -1

    if init_guess == None:
        init_guess = np.linalg.lstsq(nx.incidence_matrix(G, oriented=True).toarray(), L)[0]
    A = init_guess.copy().astype(float)
    for i in range(n):
        for u in cycles:
            R = np.array([G[j[0]][j[1]]['weight'] for j in u])
            D = np.array(edge_dir[u[:,0], u[:,1]])
            C = np.array(A[edge_idx[u[:,0], u[:,1]]])
            C = C*D
            dV = (R*C).sum()
            di = dV/R.sum()
	    C = (C - di)*D
	    A[edge_idx[u[:,0], u[:,1]]] = C
    return A

# SAMPLE INPUT DATA

G = nx.Graph()
nodes = range(6)
loads = [-180, 50, 30, 30, 50, 20]
edges = np.array([(0,1), (0,5), (1,2), (1,4), (2,3), (3,4), (4,5)])
weights = [1, 1, 1, 7.5, 1, 1, 1]

for i in range(len(nodes)):
    G.add_node(nodes[i], demand=loads[i])

for i in range(len(edges)):
    G.add_edge(*edges[i], weight=weights[i])

init_guess = np.array([80, 100, 20, 10, -10, -40, -80], dtype=float)
A = init_guess.copy()
