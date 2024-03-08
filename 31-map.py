# map, se usa para transformar elementos
numbers = [1, 2, 3, 4]
numbersV2 = []
for i in numbers:
    numbersV2.append(i * 2)
print(numbersV2)

'''con map y lambda'''
numbersV3 = list(map(lambda i : i * 2, numbers))
print(numbersV3)

'''iterando dos listas con map'''
numbers1 = [1, 2, 3, 4]
numbers2 = [5, 6, 7, 8]
result = map(lambda x,y : x + y, numbers1, numbers2)
print(list(result))