from node import *


def solve_branch_and_bound_DFS(capacity, items, record_visiting_order=False):
    """"
    :param capacity: capacidad de la mochila
    :param items: items de la mochila
    :param record_visiting_order: activa/desactiva el registro de nodos visitados
    :return: best_value, taken, visiting_order
    """

    visiting_order = []

    root_node = Node(index=0, taken=[], value=0, room=capacity)
    best_node = root_node
    best_value = 0

    def dfs(node):
        nonlocal best_value, best_node

        if node.room < 0:
            return

        if node.estimate(items) <= best_value:
            return

        if node.value > best_value:
            best_value = node
            best_node = node

        if node.index != len(items):
            dfs(Node(node.current + 1, node.taken, node.value, node.room))
            dfs(Node(node.current + 1, node.taken + [node.index + 1], node.value + items[node.index].value, node.room - items[node.index].weight))

    dfs(root_node)



    return 0, [], visiting_order