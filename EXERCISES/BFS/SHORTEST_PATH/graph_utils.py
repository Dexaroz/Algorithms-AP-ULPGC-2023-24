import networkx as nx

def build_graph():
    # Añade aqui el código que hiciste en el ejercicio del
    # apartado anterior para crear un grafo no-dirigido.

    first_line = input().split()
    num_nodes = int(first_line[0])
    num_edges = int(first_line[1])

    graph = nx.Graph()

    for i in range(1, num_nodes + 1):
        graph.add_node(i)

    for i in range(0, num_edges):
        line = input().split()
        v = int(line[0])
        u = int(line[1])
        graph.add_edge(v, u)

    return graph