# leer un archivo
file = open('./archivo.txt')
# print(file.read())
print(file.readline())

# cerrar un archivo luego de leerlo
file.close()


file = open('./archivo.txt')
for line in file:
    print(line)

# file.close()


# cerrrar archivo automaticamente luego de usar
with open("./archivo.txt") as file:
    print(file.read())