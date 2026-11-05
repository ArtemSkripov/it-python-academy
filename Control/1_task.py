# Пользователь вводит последовательность целых чисел
# через пробел.
# Например:
# 5 8 -2 10 3 8 10
# Необходимо:
# 1. получить список чисел;
# 2. вывести:
# ○
# максимальное число;
# ○
# минимальное число;
# ○
# сумму всех положительных чисел;
# 3. вывести список уникальных чисел в порядке
# возрастания.
# Нельзя использовать max(), min() и sum().

chisla = input()
l_chisla = []

for x in chisla.split():
    l_chisla.append(int(x))

max_chislo = l_chisla[0]

for x in l_chisla:
    if x > max_chislo:
        max_chislo = x
        
min_chislo = l_chisla[0]

for x in l_chisla:
    if x < min_chislo:
        min_chislo = x

sum_chislo = 0      
for x in l_chisla:
    if x > 0:
        sum_chislo += x

l_chisla_set = sorted(set(l_chisla))

print(max_chislo)       
print(min_chislo)       
print(sum_chislo)
print(l_chisla_set)
       

