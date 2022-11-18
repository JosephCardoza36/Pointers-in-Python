import random
from ctypes import *

def find_sum(num_list):
    total = 0
    for num in num_list:
        pi = pointer(num)
        print(f"{num.value} pointer: ", addressof(pi))
        total += num.value
    return total


print("*****************************************")
print("| Joseph's Random Function Integer Adder |")
print("*****************************************")

value1 = c_int(random.randint(1, 100))
value2 = c_int(random.randint(1, 100))
value3 = c_int(random.randint(1, 100))
value4 = c_int(random.randint(1, 100))
value5 = c_int(random.randint(1, 100))

value_list = [value1, value2, value3, value4, value5]

print(
    f"The random numbers are: {value1.value}, {value2.value}, {value3.value}, {value4.value}, {value5.value}")

print(f"The sum of these five Integers is {find_sum(value_list)}")
