

# squares = []
#
# for x in range(1, 6):
#     squares.append(x ** 2)
#
# print(squares)

# [выражение for элемент in последовательность if условие]
# squares = [x ** 2 for x in range(1, 6)]
# print(squares)
#
#
# even_squares = [x ** 2 for x in range(1, 11) if x % 2 != 0]
# print(even_squares)
#
#
# # Если число четное — оставляем, если нечетное — заменяем на -1
# labels = [x if x % 2 == 0 else -1 for x in range(1, 6)]
# print(labels)


matrix = [[1, 2], [3, 4]]

for row in matrix:
    for num in row:
        print(num, end=" ")

print()

# Вытягиваем вложенный список в плоский [1, 2, 3, 4]
flat = [num for row in matrix for num in row]
print(flat)
