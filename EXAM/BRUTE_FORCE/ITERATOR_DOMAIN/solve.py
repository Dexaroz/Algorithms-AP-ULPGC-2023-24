
def next_number(digits, digits_values):

    next_digits = digits.copy()
    next_digits = next_digits[::-1]
    digits_values = digits_values[::-1]

    index = 0
    while next_digits[index] == digits_values[index][-1]:
        next_digits[index] = digits_values[index][0]
        index += 1

        if index == len(next_digits) - 1:
            break

    if next_digits[index] == digits_values[index][-1] and index == len(next_digits) - 1:
        for i in range(0, len(next_digits)):
            next_digits[i] = digits_values[i][0]
            return next_digits[::-1]

    pos = digits_values[index].index(next_digits[index]) + 1
    next_digits[index] = digits_values[index][pos]

    return next_digits[::-1]

class My_Iterator:

    def __init__(self, num_digits, digits):
        self.current = []
        self.stop = []
        for i in range(0, num_digits):
            self.current.append(digits[i][0])

        for i in range(0, num_digits):
            self.stop.append(digits[i][-1])

        self.digits = digits

    def next(self):

        while self.current != self.stop:
            yield self.current
            self.current = next_number(self.current, self.digits)

        yield self.current
