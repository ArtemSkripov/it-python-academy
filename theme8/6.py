from math import sqrt

def apply_operation(x: int, y: int, operation_func) -> int:
    """Принимает функцию operation_func и применяет её к x и y."""
    return operation_func(x, y)


def multiply(a: int, b: int) -> int:
    return a * b

def summ(a: int, b: int) -> int:
    return a + b

def sqr(a: int, b: int) -> int:
    return (a + b) ** 0.5


# Передаем функцию multiply как обычный аргумент (БЕЗ скобок!)
result = apply_operation(3, 5, multiply)
# print(result)
# print(apply_operation(3, 5, summ))
print(apply_operation(3, 6, sqr))
