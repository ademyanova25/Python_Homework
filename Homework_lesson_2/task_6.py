products = []
while input('Добавить товар? (да/нет) ') == 'да':
    products.append(tuple((int(input('Введите номер товара: ')),
                          dict({'название': input('Введите название: '),
                                'цена': float(input('Введите цену: ')),
                                'количество': int(input('Введите количество: ')),
                                'eд': input('Введите единцу измерения: ')}))))

analytics = {}
for product in products:
    for ch_key, ch_value in product[1].items():
        if ch_key in analytics:
            if ch_value not in analytics.get(ch_key):
                analytics[ch_key].append(ch_value)
        else:
            analytics[ch_key] = [ch_value]
print(analytics)
