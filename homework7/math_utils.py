# Задание 2
# Создайте файл math_utils.py.
# Реализуйте функции:
# square(number)
# cube(number)
# is_even(number)
# factorial(number)
# max_of_two(a, b)
# Запрещается использовать встроенные функции max() и
# math.factorial().
# После создания файла импортируйте функции в другой
# программе и продемонстрируйте их работу.


def square(number):
    
    x=number**2
    return x

def cube(number):
    
    x=number**3
    return x

def is_even(number):
    
    if number % 2 == 0:
        x = True
    else:
        x = False  
    return x

def factorial(number):
    
    if number == 1:
        return 1
    return number * factorial(number -1)

def max_of_two(a,b):
    
    max = 0
    if a > b:
        max = a
    elif b > a:
        max = b
    else:
        max = 'Они равны'
         
    return max
