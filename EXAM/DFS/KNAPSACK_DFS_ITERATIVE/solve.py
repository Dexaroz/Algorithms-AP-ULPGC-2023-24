from simple_stack import Stack

def solve(items, capacity):
    solutions_list = []
    best_value = 0
    stack = Stack()

    def dfs():
        nonlocal solutions_list, best_value

        index = 0
        taken = []
        value = 0
        weight = 0
        stack.push((index + 1, value, weight, list(taken)))

        while not stack.isEmpty():

            index, value, weight, taken = stack.pop()

            if index == len(items):
                if value > best_value:
                    solutions_list = list(taken)
                    best_value = value
                elif value == best_value:
                    solutions_list.append(list(taken))
            else:
                stack.push((index + 1, value, weight, list(taken)))

                if weight + items[index][1] <= capacity:
                    taken.append(index + 1)
                    stack.push((index + 1, value + items[index][0], weight + items[index][1], taken))


    dfs()
    return solutions_list, best_value

