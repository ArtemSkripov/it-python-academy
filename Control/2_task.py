# Задание 2
# Пользователь вводит предложение.
# Необходимо написать функцию
# analyze_text(text)
# которая возвращает словарь следующего вида:
# {
# "words": ...,
# "letters": ...,
# "longest_word": …,
# "shortest_word": ...,
# "unique_words": ...
# }
# где:
# ●
# words — количество слов;
# ●
# letters — количество букв (без учета пробелов);
# ●
# longest_word — самое длинное слово.
# ●
# shortest_word — самое короткое слово;
# ●
# unique_words — количество различных слов без учета
# регистра.
# Запрещается использовать регулярные выражения и
# сторонние библиотеки. Нельзя использовать функцию max


def analyze_text(text):
    
    if not text:
        print('Нет текста!')
        return
    
    keys= ['words','letters','longest_word','shortest_word','unique_words']
    big_text=dict.fromkeys(keys)
    
    text_list = text.split()
    text_words = text.replace(" ", "")
    
    for x in text:
        text_words += x
        
    longest = text_list[0]
    for x in text_list:
        if len(x) > len(longest):
            longest = x
            
    shortest = text_list[0]
    for x in text_list:
        if len(x) < len(shortest):
            shortest = x
            
    lower_words = []
    for x in text_list:
        lower_words.append(x.lower())
    
    big_text['words'] = len(text_list)
    big_text['letters'] = len(text_words)
    big_text['longest_word'] = longest
    big_text['shortest_word'] = shortest
    big_text['unique_words'] = len(set(lower_words))
    
    
    return big_text

user_text = input()
result = analyze_text(user_text)
print(result)