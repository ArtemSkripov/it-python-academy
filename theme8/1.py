data = [1, 2, 3, 4, 5]

# ИМПЕРАТИВНЫЙ СТИЛЬ: Пошагово управляем индексами и состоянием
result_imp = []
for x in data:
    if x % 2 == 0:
        result_imp.append(x * 10)

# ДЕКЛАРАТИВНЫЙ СТИЛЬ: Описываем суть трансформации
result_decl = [x * 10 for x in data if x % 2 == 0]
