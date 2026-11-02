sessions = [
    {"user": "alex_99", "failed_attempts": 3, "is_admin": False},
    {"user": "root_admin", "failed_attempts": 0, "is_admin": True},
    {"user": "dev_tester", "failed_attempts": 5, "is_admin": False},
    {"user": "sec_officer", "failed_attempts": 2, "is_admin": True}
]
# Отсортируйте список sessions по убыванию количества неудачных попыток входа (failed_attempts),
# используя встроенную функцию sorted() и lambda в параметре key.

# Напишите вторую сортировку с lambda, которая сгруппирует пользователей так,
# чтобы сначала шли обычные пользователи (is_admin == False), а затем администраторы.


print(sorted(sessions, key=lambda x: x["failed_attempts"], reverse=True))
print(sorted(sessions, key=lambda x: x["is_admin"]))
