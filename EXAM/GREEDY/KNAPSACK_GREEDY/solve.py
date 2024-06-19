def solve(items, capacity):
    taken = []
    value = 0

    items_sorted = sorted(items, key=lambda x: x[0]/x[1], reverse=True)

    index = 0
    while index != len(items) and capacity != 0:
        item = items_sorted[index]
        if item[1] <= capacity:
            value += item[0]
            taken.append(item)
            capacity -= item[1]
        index += 1

    solution = []
    for item in taken:
        index = items.index(item)
        solution.append(index + 1)

    return solution, value
