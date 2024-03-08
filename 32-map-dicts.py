# 
items = [
    {
        'product': 'camisa',
        'price': 300
    },
    {
        'product': 'pantalones',
        'price': 100
    },
    {
        'product': 'corbata',
        'price': 200
    },
]

prices = list(map(lambda item: item['price'], items))
print(prices)

''''''
def addTaxes(item):
    item['taxes'] = item['price'] * .19
    return item

newItems = list(map(addTaxes, items))
print(newItems)
