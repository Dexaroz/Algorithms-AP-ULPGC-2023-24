from solve import *

first_line = input().split()
num_digits = int(first_line[0])

digit_values = []
for j in range(num_digits):
    line = input().split()     # domain values of each digit
    int_values = []
    for value in line:
        int_values.append(int(value))
    digit_values.append(int_values)

obj = My_Iterator(num_digits, digit_values)
for c in obj.next():
     print(c)
