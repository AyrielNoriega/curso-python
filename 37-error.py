suma = lambda x,y : x + y
assert suma(2, 2) == 4
assert suma(2, 2) == 4, 'No es igual'

age = 10
if age > 18:
    raise Exception('No se permite menors a 18')

try:
    print(0/0)
except ZeroDivisionError as error:
    print(error)

try:
    if age < 18:
        raise Exception('No se permite menors a 18')
except Exception as error:
    print(error)