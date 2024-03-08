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

'''no modificar el estado del array original con map'''
def addTaxes(item):
    newItem = item.copy()
    newItem['taxes'] = newItem['price'] * .19 ##creamos nuevo item, con eso no modificados el array principal
    return newItem

newItems = list(map(addTaxes, items))
print(items)
print(newItems)
