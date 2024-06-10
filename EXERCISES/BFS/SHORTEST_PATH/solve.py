import networkx   as nx
from sys          import maxsize as infinite
from simple_queue import *

def bfs_path_length(graph, first_node):
    """
    Compute the shortest path length of the non-directed graph G
    starting from node first_node. Return a dictionary with the
    distance (in number of steps) from first_node to all the nodes.
    """

    distance = {}                 # Diccionario con la distancia desde
    visible = []                  # firstNode al resto de los nodos.
    queue = Queue()

    for node in graph.nodes():
        distance[node] = infinite

    # solve it here!
    # ...
    queue.enqueue(first_node)
    visible.append(first_node)
    distance[first_node] = 0


    while not queue.isEmpty():
        v = queue.dequeue()

        for neighbor in graph.neighbors(v):
            if neighbor not in visible:
                visible.append(neighbor)
                distance[neighbor] = distance[v] + 1
                queue.enqueue(neighbor)

    return distance