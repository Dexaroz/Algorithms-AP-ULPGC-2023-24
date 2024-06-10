import matplotlib.pyplot as plt
import networkx as nx
from solve import *

graph = build_graph();

print("Number of nodes: " + str(graph.number_of_nodes()))
print("Nodes: ", graph.nodes())
print("Number of edges: " + str(graph.number_of_edges()))
print("Edges: ", graph.edges())

# Paso 3 (Opcional): En PyCharm añade aqui el código necesario
#        para mostrar gráficamente el grafo.
# ...
nx.draw(graph, node_color = 'black', edge_color='red')
plt.show()