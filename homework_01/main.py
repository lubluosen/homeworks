"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    return [i ** 2 for i in args]


print(power_numbers(1, 2, 5, 7))


# filter types
from sympy import isprime
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(num_list, p):
    result = []
    for num in num_list:
        if p == "odd" and num % 2 != 0:
            result.append(num)
        elif p == "even" and num % 2 == 0:
            result.append(num)
        elif p == "prime" and isprime(num):
            result.append(num)
    return result


print(filter_numbers([5, 8, 3, 6, 9], PRIME))

