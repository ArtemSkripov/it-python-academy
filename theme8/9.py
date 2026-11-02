from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

# 1. map: Преобразуем каждое число в его квадрат
squares = list(map(lambda x: x ** 2 if x % 2 == 0 else x**3, numbers))
# print(squares)
# print([x ** 2 if x % 2 == 0 else x**3 for x in numbers])

# 2. filter: Оставляем только четные числа
evens = list(filter(lambda x: x % 2 == 0, numbers))
# print(evens)
# print([x for x in numbers if x%2==0])


# Вычисление произведения: ((1 * 2) * 3) * 4  (((10 * 1) * 2) * 3) * 4
product = reduce(lambda x, y: x * y, numbers, initial=10)
# print(product)


words = ["python", "c", "javascript", "go"]
# Сортировка по длине слова, а не по алфавиту
sorted_words = sorted(words, key=len)
# print(sorted_words)


numbers2 = [5, 1, -3, 2, 4, -6]
sorted_numbers2 = sorted(numbers2, key=abs)
print(sorted_numbers2)


users = {
    
}

