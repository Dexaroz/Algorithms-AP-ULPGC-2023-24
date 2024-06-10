# Versión 1

def order_crossover(parent1, parent2, lower_bound, upper_bound):
    child1 = []

    for i in range(lower_bound, upper_bound):
        child1.append(parent1[i])

    index = 0
    for i in range(upper_bound, len(parent1)):
        if parent2[i] not in child1:
            child1.append(parent2[i])
            index += 1

    index2 = 0
    while ((upper_bound - lower_bound) + index) != (len(parent1) - lower_bound):
        if parent2[index2] not in child1:
            child1.append(parent2[index2])
            index += 1
        index2 += 1

    index = 0
    for i in range(0, len(parent1)):
        if parent2[i] not in child1:
            child1.insert(index, parent2[i])
            index += 1

    return child1

#Versión 2
def order_crossover2(parent1, parent2, lower_bound, upper_bound):
    child1 = []

    for i in range(0, len(parent1)):
        if (i >= lower_bound) and (i < upper_bound):
            child1.append(parent1[i])
        else:
            child1.append(None)

    index = 1
    for i in range(upper_bound, len(child1)):
        if parent2[i] not in child1:
            child1[i] = parent2[i]
            index += 1

    index2 = 0
    while index != len(child1) - upper_bound + 1:
        if parent2[index2] not in child1:
            child1[index + upper_bound - 1] = parent2[index2]
            index += 1
        index2 += 1

    for i in range(0, lower_bound):
        if parent2[index2] not in child1:
            child1[i] = parent2[index2]
        index2 += 1

    return child1