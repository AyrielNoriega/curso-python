# listas o arrays

numbers = [1, 2, 3, 4, 5]
print(numbers)
print(type(numbers))

print(2 in numbers)

'''reasignar valor al ultimo elemento de una lista'''
numbers[-1] = 10
print(numbers)

'''agregar o insertar elementos a una lista, lo agrega al final de la lista'''
numbers.append(700)
print(numbers)

'''insertar elementos en una lista en un index indicado'''
numbers.insert(0, 'cero')
print(numbers)

'''concatenar listas o arrays'''
othersNumbers = [11, 12, 13]
newList = numbers + othersNumbers
print(newList)

'''saber posicion de un elemento'''
print(newList.index('cero'))

'''eliminar un elemento de una lista'''
othersNumbers = [11, 12, 13]
othersNumbers.remove(13)
print(othersNumbers)


'''eliminar el ultimo elemento de la lista'''
othersNumbers.pop()
print(othersNumbers)

'''eliminar el ultimo elemento de la lista en una posición indicado por el index, parecido a remove'''
numbers.pop(0)
print(numbers)

'''invertir valores de lista'''
numbers.reverse()
print(numbers)

'''ordenar valores de lista,  aplica para string también:; no aplica para tipos de datos mezclados'''
numbers.sort()
print(numbers)
