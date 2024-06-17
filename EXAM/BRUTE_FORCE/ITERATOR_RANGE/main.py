from solve import *

first_line   = input().split()
num_digits   = int(first_line[0])    # Number of digits
second_line  = input().split()       # min values of each digit
min_values   = []
for j in range(num_digits):
    min_values.append(int(second_line[j]))
third_line   = input().split()       # max values of each digit
max_values   = []
for j in range(num_digits):
    max_values.append(int(third_line[j]))

obj = My_Iterator(num_digits, min_values, max_values)
for c in obj.next():
     print(c)
