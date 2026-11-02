def validate_text(text: str, *validators) -> bool:
    for validator in validators:
        if not validator(text):
            return False

    return True

def is_long_enough (text: str) -> bool:
    return len(text)>=8

def has_no_spaces (text: str) -> bool:
    return " " not in text

def is_capitalized (text: str) -> bool:
    return bool(text) and text[0].isupper()

# Тестирование конвейера
print(validate_text("Superpass123", is_long_enough, has_no_spaces, is_capitalized))
print(validate_text("weak pass", is_long_enough, has_no_spaces))
print(validate_text("",  is_capitalized))