import networkx  as nx

from graph_utils import *
from solve       import *

graph = build_graph();

first_node = 1
last_node  = graph.number_of_nodes()

route = bfs_path(graph, first_node, last_node)
print(route)