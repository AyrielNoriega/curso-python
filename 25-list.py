# List Comprehension, una forma de generar listas con una sintaxis mas corta.

'''normalmente haríamos:'''
numbers = []
for element in range(1, 11):
    numbers.append(element)
print(numbers)

# con list Comprehension
numbers2 = [element for element in range(1, 11)]
print(numbers2)

numbers2 = [element * 2 for element in range(1, 11)]
print(numbers2)

# agregando condiciones
numbers2 = [element * 2 for element in range(1, 11) if element % 2 == 0]
print(numbers2)