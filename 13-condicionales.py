# if
if True:
    print('ejecutando if')

if False:
    print('ejecutando if')
elif False:
    print('No se ejecuta')
else:
    print('ejecutando else')

numero = input('numero ')
if int(numero) == 1:
    print(f'numero es { numero }')