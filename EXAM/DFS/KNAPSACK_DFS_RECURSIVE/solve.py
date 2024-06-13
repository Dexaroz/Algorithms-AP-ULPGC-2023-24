def solve(items, capacity):
    solution = []
    best_value = 0

    def dfs(index, value, weight, taken):
        nonlocal solution, best_value

        if index == len(items):
            if value > best_value:
                solution = list(taken)
                best_value = value
            return

        item_value = items[index][0]
        item_weight = items[index][1]

        dfs(index + 1, value, weight, taken)

        if weight + item_weight <= capacity:
            taken.append(index + 1)
            dfs(index + 1, value + item_value, weight + item_weight, taken)
            taken.pop()

    dfs(0, 0, 0, [])
    return solution, best_value