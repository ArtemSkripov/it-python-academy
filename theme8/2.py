
# ПЛОХО (НЕчистая функция с побочным эффектом):
total = 0
def add_to_total(amount):
    global total
    total += amount  # Изменяет внешнее состояние!

# ХОРОШО (Чистая функция):
def calculate_total(current_total: float, amount: float) -> float:
    return current_total + amount * 0.1 # Только возвращает новое значение
