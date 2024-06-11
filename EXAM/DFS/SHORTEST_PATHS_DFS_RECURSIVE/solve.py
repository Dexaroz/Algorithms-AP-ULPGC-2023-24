import networkx as nx
from sys import maxsize as infinite

def solve(graph, u, v):
    solutions_list = []
    min_dist = infinite
    visitedNodes = set()

    def dfs(graph, u, solution, dist):
        nonlocal min_dist, solutions_list

        visitedNodes.add(u)
        solution.append(u)

        if u == v:
            if dist < min_dist:
                min_dist = dist
                solutions_list.clear()
                solutions_list.append(list(solution))
            elif dist == min_dist:
                solutions_list.append(list(solution))
            solution.pop()
            visitedNodes.remove(u)
            return

        for neighbor in graph.neighbors(u):
            if neighbor not in visitedNodes:
                dist += graph.edges[u,neighbor]['weight']

                if dist <= min_dist:
                    dfs(graph, neighbor, solution, dist)
                dist -= graph.edges[u,neighbor]['weight']
        solution.pop()
        visitedNodes.remove(u)


    dfs(graph, u, [], 0)

    return solutions_list