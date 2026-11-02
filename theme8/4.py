# 1. Set Comprehension (Автоматически удаляет дубликаты)
# unique_lengths = {len(word) for word in ["python", "java", "python", "go"]}
# print(unique_lengths)

# 2. Dict Comprehension (Генератор словарей)
# users = ["alex", "maria", "john"]
# DEFAULT_ID = 100
# user_ids = {user: i for i, user in enumerate(users, start=DEFAULT_ID)}
# print(user_ids)


# 3. Выражение-генератор (Generator Expression) — Круглые скобки!
# Не создает список в памяти сразу, а вычисляет элементы «на лету» (лениво)
sum_large = sum(x ** 2 for x in range(1_000_000))

print(sum_large)

# for x in sum_large:
#     print(x)
#
# print("вторая итерация")
# for x in sum_large:
#     print(x)

# квадраты нечетных чисел, или строка "четное" для чётных
lll = [x**2 if x % 2 == 0 else x**3 if x % 3 == 0 else x for x in range(1, 21) if x % 10 != 0]
print(lll)

res = []
for x in range(1, 21):
    if x % 10 == 0:
        continue

    if x % 2 == 0:
        res.append(x**2)
    elif x % 3 == 0:
        res.append(x**3)
    else:
        res.append(x)

print(res)