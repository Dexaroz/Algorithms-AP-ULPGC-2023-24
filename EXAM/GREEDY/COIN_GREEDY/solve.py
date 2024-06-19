from sys import maxsize as infinite


def solve(coins, change):
    taken = []
    sorted_coins = sorted(coins, reverse=True)

    index = 0
    while index != len(coins) and change != 0:
        if sorted_coins[index] <= change:
            taken.append(sorted_coins[index])
            change -= sorted_coins[index]
        index += 1

    solution = []
    for coin in taken:
        index = coins.index(coin)
        solution.append(index + 1)
        coins[index] = None

    return solution
