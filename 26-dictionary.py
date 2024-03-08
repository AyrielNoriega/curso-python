# Dictionary Comprehension

dict = {}
for i in range(1, 11):
    dict[i] = i * 2
print(dict)

'''con Dictionary Comprehension'''
dict2 = {i: i * 2 for i in range(1, 11)}
print(dict2)

''''''
import random

countries = ['col', 'pe', 'cad']
population = {}
for country in countries:
    population[country] = random.randint(1, 100)

print(population)

'''el ejercicio anterior se puede escribir mejor asi:'''
countries = ['col', 'pe', 'cad']
populationV2 = { country: random.randint(1, 100) for country in countries }
print(populationV2)


'''union entre listas'''

names = ['nico', 'zule', 'santi']
ages = [12, 45, 21]

union = zip(names, ages)
listNames = list(union)
print(zip(names, ages))
print(listNames)

#generando diccionario de listNames
newDict = { name: age for (name, age) in listNames }
print(newDict)
print(list(newDict))
