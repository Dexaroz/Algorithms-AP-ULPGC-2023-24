from sys import maxsize as infinite
from simple_stack import Stack

def solve(coins, change):
    solution = []
    best_value = 0

    def dfs():
        nonlocal solution, best_value

        taken = []
        value = 0
        stack = Stack()
        index = 0

        stack.push((index, value, list(taken)))

        while not stack.isEmpty():

            index, value, taken = stack.pop()

            if index == len(coins):
                if value > best_value:
                    solution = list(taken)
                    best_value = value
            else:
                stack.push((index + 1, value, list(taken)))

                if coins[index] + value <= change:
                    taken.append(index + 1)
                    stack.push((index + 1, value + coins[index], list(taken)))

        return

    dfs()

    return solution
