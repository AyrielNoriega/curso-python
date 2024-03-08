
# definiendo funciones

def  myPrint():
    print('this is my print')

myPrint()

def  myPrint(name):
    print(f'this is my {name}')

myPrint('Ayriel')

# funcion con retorno de valores
def  findVolume(length=1, width=1, depth=1):
    return length * width * depth

volume = findVolume(width=2)
print(volume)

# retornar multiples valores en una funcion
def  findVolume(length=1, width=1, depth=1):
    return length * width * depth, width, 'otro valor' ### aqui indicamos los valors que queremos retornar

volume = findVolume(width=2)
print(volume)

'''extraer valores, en el orden en que fueron declarados en el return de la funcion'''
volume, width, text = findVolume(width=3)
print(volume)
print(width)
print(text)

