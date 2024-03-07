''' los conjuntos no tienen un par key-value; elimina los elementos duplicados; puede tener elementos mixtos 
o distintos tipos de datos.
El set se ordena asi mismo.
 
'''
set_countries = {'col', 'mex', 'bol'}
print(set_countries)
print(type(set_countries))


set_types = {1, 'hola', False, 12.12}
print(set_types) # {False, 1, 12.12, 'hola'}


# la podemos crear a partir de un string
set_from_string = set('hoola')
print(set_from_string) # {'a', 'l', 'o', 'h'}


# la podemos crear a partir de una tupla
set_from_tuples = set (('abc','cbv','as','abc'))
print(set_from_tuples) # {'as', 'abc', 'cbv'}

# la podemos crear a partir de una lista
numbers = [1,2,3,1,2,3,4]
set_numbers= set(numbers)
print(set_numbers) # {1, 2, 3, 4}
# si quiero convertir este set único a una lista, lo puedo hacer:
unique_numbers = list(set_numbers)
print(unique_numbers)


# agregar un elemento al conjunto
set_countries = {'col', 'mex', 'bol'}
set_countries.add('pe')
print(set_countries)
# actualizar un conjunto
set_countries.update({'pe', 'arg', 'ecu'})
print(set_countries)

# eliminar elemento de un conjunto
set_countries.remove('col')
print(set_countries)

set_countries.discard('eu')
print(set_countries)

set_countries.clear()
print(set_countries)