# reduce, reduce una lista en un solo valor
import functools ##hay que importar esto para usar reduce
numbers = [1, 2, 3, 4]
result = functools.reduce(lambda counter, item : counter + item, numbers)
print(result)