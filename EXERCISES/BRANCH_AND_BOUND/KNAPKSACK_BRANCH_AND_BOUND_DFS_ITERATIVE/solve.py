from node import *


def solve_branch_and_bound_DFS(capacity, items, record_visiting_order=False):
    """"
    :param capacity: capacidad de la mochila
    :param items: items de la mochila
    :param record_visiting_order: activa/desactiva el registro de nodos visitados
    :return: Por ahora sólo devuelve la lista de nodos visitados
    """

    # Completa este código para realizar el recorrido DFS; tienes
    # indicados los sitios que debes completar con tres puntos
    # suspensivos ("...")

    # Utilizamos la lista 'alive' como nuestra pila de nodos vivos
    # (pendientes de visitar) para programar nuestro recorrido DFS.

    alive = []

    # Utilizamos la lista Visiting_Order como el registro de nodos
    # visitados (el contenido final de esta lista lo utiliza el VPL
    # para comprobar que nuestro recorrido DFS es correcto).

    visiting_order = []

    # 1) Creamos el nodo raiz.
    node = Node(0, [], 0, capacity)

    # Lo añadimos a la lista de nodos vivos (alive)
    alive.append(node)

    # Mientras haya nodos en la lista de nodos vivos
    # ...
    best_value = 0
    best_node = node

    while len(alive) != 0:
        # Avanzamos al siguiente nodo de nuestro recorrido DFS (hacemos un pop
        # de la lista) y lo registramos en nuestro recorrido DFS.

        current = alive.pop()
        if record_visiting_order:
            visiting_order.append(current.index)
        # Condiciones de poda
        # ...
        if current.room < 0:
            continue
            ###

        if current.estimate(items) <= best_value:
            continue
            ###

        if current.value > best_value:
            best_value = current.value
            best_node = current


        # Si no hemos llegado al final del árbol
        #    1) Ramificamos (branch) por la derecha (append)
        #    2) Ramificamos (branch) por la izquierda (append)
        if current.index < len(items):
            alive.append(Node(current.index + 1,
                              current.taken,
                              current.value,
                              current.room))
            alive.append(Node(current.index + 1,
                              current.taken.copy() + [current.index + 1],
                              current.value + items[current.index].value,
                              current.room - items[current.index].weight))

    return best_node.value, best_node.taken, visiting_order