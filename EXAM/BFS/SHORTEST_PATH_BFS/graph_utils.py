import networkx as nx

def build_graph():
    """
    Read data from the standard input and build the corresponding
    nondirected graph without weights. Nodes numbering starts with
    number 1 (that is, nodes are 1,2,3,...)
    """
    first_line = input().split()
    num_nodes  = int(first_line[0])
    numEdges   = int(first_line[1])

    # Crear grafo unidirecional con num_nodes
    G = nx.Graph()
    G.add_nodes_from(range(1,num_nodes+1))

    # Añadir los vértices del grafo
    for j in range(1, numEdges+1):
        parts = input().split()

        u = int(parts[0])
        v = int(parts[1])
        G.add_edge(u, v)

    return G
