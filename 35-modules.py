# puedo preguntar por el sistema operativo
import sys

print(sys.path)  ##nos muestra la ruta del archivo desde donde se esta ejecutando el comando

# re: tiene que ver con expresiones regulares
import re

text = 'Mi numero es 112 1212 1212, el codigo del pais es 57'
result = re.findall('[0-9]+', text) ##con esto buscamos en el texto solo los numeros encontrados
print(result)

# time: manejo de horas y fechas
import time
timestamp = time.time()
local = time.localtime()
result = time.asctime(local)
print(result)

# collections: para manejar listas
import collections
numbers = [1, 2, 3, 4, 5, 6, 1, 1, 2, 2]
counter = collections.Counter(numbers) ##en este caso, nos muestra la cantidad de repeticiones que tiene un numero en la lista
print(counter)