# while
'''
while False:
    print('ejecutando')

counter = 0

while counter <= 10:
    counter += 1
    print(counter)

counter = 0

while counter < 10:
    counter += 1

    if counter == 5:
        continue

    print(counter)
'''

for element in range(50):
    print(element)

myList = [1, 2, 3, 4, 5]
for element in myList:
    print(element)

product = {
    'name': 'camisa',
    'price': 100,
    'stock': 90
}
for element in product:
    print(element)

for key, value in product.items():
    print(value)
