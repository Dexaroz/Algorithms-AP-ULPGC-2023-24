def solve(houses):
    solution = []
    max_money = 0

    def dfs(index, value, taken):
        nonlocal solution, max_money

        if index == len(houses):
            if value > max_money:
                solution = list(taken)
                max_money = value
            return

        dfs(index + 1, value, taken)

        if (index + 1) + 1 not in taken and (index + 1) - 1 not in taken:
            taken.append(index + 1)
            dfs(index + 1, value + houses[index], taken)
            taken.pop()

    dfs(0, 0, [])

    return solution, max_money