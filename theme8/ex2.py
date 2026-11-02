catalog = {"Phone": 1200, "Case": 150, "Tablet": 800, "Laptop": 2000}

discounted_catalog = {price*0.8 for product, price in catalog.items() if price > 1000}

print(discounted_catalog)


catalog = {"Phone": 1200, "Case": 150, "Tablet": 800, "Laptop": 2000}
discounted = {name: price * 0.8 if price > 1000 else price for name, price in catalog.items()}
print(discounted)


catalog = {"Phone": 1200, "Case": 150, "Tablet": 800, "Laptop": 2000}
discounted = {name: price * 0.8 if price > 1000 else price for name, price in catalog.items() }
print(discounted)
