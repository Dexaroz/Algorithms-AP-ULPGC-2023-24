
def next_number(digits, min_values, max_values):

    next_digits = digits.copy()
    next_digits = next_digits[::-1]

    min_values = min_values[::-1]
    max_values = max_values[::-1]

    index = 0
    while next_digits[index] == max_values[index]:
        next_digits[index] = min_values[index]
        index += 1

        if index == len(digits) - 1:
            break

    if index == len(digits) - 1 and next_digits[index] == max_values[index]:
        return min_values

    next_digits[index] += 1
    return next_digits[::-1]

class My_Iterator:

    def __init__(self, num_digits, min_values, max_values):
        self.current = min_values
        self.stop = max_values
        self.min_values = min_values
        self.num_digits = num_digits

    def next(self):
        while self.current != self.stop:
            yield self.current
            self.current = next_number(self.current, self.min_values, self.stop)
        yield self.current
