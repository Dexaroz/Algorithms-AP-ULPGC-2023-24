import networkx   as nx
from simple_queue import *

def bfs_path(graph, first_node, last_node):
    """
    Compute the shortest path from the first_node to the last_node
    of the non-directed graph G. Return a list with the nodes.
    """

    # solve it here!

    route = []
    visibleNodes = set()
    queue = Queue()
    distance = {}

    distance[first_node] = ([first_node], 0)
    queue.enqueue(first_node)
    visibleNodes.add(first_node)

    while not queue.isEmpty():

        v = queue.dequeue()

        for neighbor in graph.neighbors(v):
            if neighbor not in visibleNodes:
                visibleNodes.add(neighbor)
                moment_route = distance[v][0]
                distance[neighbor] = (moment_route + [neighbor], distance[v][1] + 1)
                queue.enqueue(neighbor)

    route = distance[last_node][0]

    return route