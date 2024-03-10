with open("./archivo.txt", 'r+') as file: 
    print(file.read())
    file.write('\nNueva linea')

## r+ : leer y escribir
## w+ : escritura y lestura pero sobreescribe todo el archivo
    
    