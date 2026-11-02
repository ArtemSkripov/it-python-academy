# Обычная именованная функция:
def add_def(x: int, y: int) -> int:
    return x + y

# Эквивалентная lambda-функция: lambda x, y
add_lambda = lambda x, y: x + y if x > y else y

print(add_def(3, 5))     # 8
print(add_lambda(3, 5))  # 8
