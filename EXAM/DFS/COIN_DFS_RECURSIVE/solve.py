from sys import maxsize as infinite

def solve(coins, change):
    solutions_list = []
    best_value = 0

    def dfs(index, value, taken):
        nonlocal solutions_list, best_value

        if index == len(coins):
            if value > best_value:
                solutions_list.clear()
                solutions_list.append(list(taken))
                best_value = value
            elif value == best_value:
                solutions_list.append(list(taken))
            return

        coins_taken = (coins[w - 1] for w in taken)
        dfs(index + 1, value, taken)

        if value + coins[index] <= change and coins[index] not in coins_taken:
            taken.append(index + 1)
            dfs(index + 1, value + coins[index], taken)
            taken.pop()

    dfs(0, 0, [])
    return solutions_list
