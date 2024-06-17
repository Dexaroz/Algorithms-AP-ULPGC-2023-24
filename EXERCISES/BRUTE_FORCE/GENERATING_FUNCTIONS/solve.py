# 1. Copia aqui tu solución del primer ejercicio de esta semana

def next_number(digits, base):
    """
    :param digits: list containing all the digits of a number
                   in the given base
    :param base: numeric base of the number
    :return: list representing the next value of the number

     Example: digits = [0, 1, 0, 1]   number 5
                base = 2

              returns [0, 1, 1, 0]    number 6
    """

    next_digits = digits.copy()
    next_digits = next_digits[::-1]

    # Añade tu código aqui
    # ...

    index = 0
    while next_digits[index] == base - 1:
        next_digits[index] = 0
        index += 1
        if index == len(next_digits) - 1:
            break

    if next_digits[index] == base - 1 and index == len(next_digits) - 1:
        next_digits[index] = 0
        return next_digits[::-1]

    if next_digits[index] != base - 1:
        next_digits[index] += 1

    return next_digits[::-1]


# ----------------------------------------------------------

class My_Iterator:

    def __init__(self, num_digits, base):
        self.base = base
        self.actual = [0] * num_digits
        self.stop = [base - 1] * num_digits


    def next(self):
        while self.actual != self.stop:
            yield self.actual
            self.actual = next_number(self.actual, self.base)

        yield self.actual
        return
