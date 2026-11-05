# Задание 5
# products = [
# {"name": "Хлеб"
# ,
# "price": 70,
# "count": 2},
# {"name": "Молоко"
# ,
# "price": 120,
# "count": 1},
# {"name": "Сыр"
# ,
# "price": 350,
# "count": 3},
# ]
# Написать функцию, которая возвращает
# {
# "total": ...,
# "most_expensive": ...,
# "items": ...
# }
# где
# ●
# total — общая стоимость покупки;
# ●
# most_expensive — название самого дорогого товара;
# ●
# items — общее количество товаров.

products = [
    {'name': 'Хлеб', 'price': 70, 'count': 2},
    {'name': 'Молоко', 'price': 120, 'count': 1},
    {'name': 'Сыр', 'price': 350, 'count': 3},
]

def prod_list(products_di):
    total_price = 0
    for x in products_di:
        total_price += x['price'] * x['count']
    
    total_count = 0
    for x in products_di:
        total_count += x['count']
     
    max_price = products_di[0]['price']
    expensive_name = products_di[0]['name'] 
          
    for x in products_di:
        if x['price'] > max_price:
            max_price = x['price']
            expensive_name = x['name']
            
    result = {
        'total': total_price,
        'most_expensive': expensive_name,
        'items': total_count
    }
    
    return result

print(prod_list(products))
