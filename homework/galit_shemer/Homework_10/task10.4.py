PRICE_LIST = """тетрадь 50
книга 200
ручка 100
карандаш 70
альбом 120
пенал 300
рюкзак 500"""

price_dict = {
    product: int(price)
    for product, price in (
        line.split()
        for line in PRICE_LIST.splitlines()
    )
}

for product, price in price_dict.items():
    print(f"{product}: {price}")
