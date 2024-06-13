from simple_stack import Stack

def solve(houses):
    solution = 0
    best_value = 0
    stack = Stack()

    def dfs():
        nonlocal solution, best_value

        taken = []
        value = 0
        index = 0

        stack.push((index, value, list(taken)))

        while not stack.isEmpty():

            index, value, taken = stack.pop()

            if index == len(houses):
                if value > best_value:
                    solution = list(taken)
                    best_value = value
            else:

                stack.push((index + 1, value, list(taken)))

                if (index + 1) + 1 not in taken and (index + 1) - 1 not in taken:
                    taken.append(index + 1)
                    stack.push((index + 1, value + houses[index], list(taken)))
        return

    dfs()
    return solution, best_value