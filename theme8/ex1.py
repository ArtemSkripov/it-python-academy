raw_prices = ["100$ ", " 250$", "FREE", " -50$", "500$", "0$"]

new_list = [int(x.strip().replace("$", "")) for x in raw_prices if x.strip().replace("$", "").lstrip("-").isdigit() and int(x.strip().replace("$", "")) >= 0]

print(new_list)


result = [
    int(price) for price in [_price.strip().replace("$", "") for _price in raw_prices]
    if price != "FREE" and int(price) >= 0
]

print(result)