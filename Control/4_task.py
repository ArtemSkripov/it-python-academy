# Задание 4
# Напишите функцию
# process_numbers(numbers, operation)
# которая принимает:
# ●
# список чисел;
# ●
# функцию, выполняющую преобразование одного числа.
# Функция должна вернуть новый список, содержащий
# результат применения operation к каждому элементу.
# Например:
# numbers = [1, 2, 3, 4]
# result = process_numbers(numbers, lambda x: x ** 2)
# print(result)
# Результат:
# [1, 4, 9, 16]
# Продемонстрируйте работу функции, передав ей три разные
# операции:
# ●
# квадрат;
# ●
# куб;
# ●
# модуль числа.
# 3 вызова с lambda и три функции написать самостоятельно.
# Итого 6 вызовов.


def process_numbers(numbers, operation):
    return list(map(operation, numbers))

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def module(x):
    if x < 0:
        return -x
    return x


numbers = [1, -2, 3, -4]
print(process_numbers(numbers, square))
print(process_numbers(numbers, cube))
print(process_numbers(numbers, abs))
print(process_numbers(numbers, lambda x: x ** 2))
print(process_numbers(numbers, lambda x: x ** 3))
print(process_numbers(numbers, lambda x: -x if x < 0 else x))
