"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    return [i ** 2 for i in args]


print(power_numbers(1, 2, 5, 7))


# filter types
def prime(num):
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if not num % i:
                return None
        return num
    return None


ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(num_list, num):
    result = []
    for numbers in num_list:
        if num == "odd" and numbers % 2 != 0:
            result.append(numbers)
        elif num == "even" and numbers % 2 == 0:
            result.append(numbers)
        elif num == "prime" and prime(numbers):
            result.append(numbers)
    return result


print(filter_numbers([5, 8, 3, 6, 9], PRIME))
