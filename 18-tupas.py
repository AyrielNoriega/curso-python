# una tupla no puede ser modificada a diferencia de una lista; es la principal diferencia entre una lista

numbers = (1, 2, 3, 4, 5)
print(numbers)

print(type(numbers))

print(numbers.index(2))
print(numbers.count(2))


'''transformar una tupla a una lista'''
myList = list(numbers)
myList.append(100)
print(myList)
print(type(myList))

'''transformar una lista a una tupla'''
numbers = tuple(myList)
print(numbers)
print(type(numbers))