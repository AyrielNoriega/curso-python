# concatenacion
name = 'Ayriel'
lastName = 'Noriega'

print(name + ' ' + lastName)

quote = "I'm Ayriel"
print(quote)

# formato / format

template = "Hola mi nombre es " + name
print('v1', template)

template = "Hola mi nombre es {}".format(name)
print(template)

template = f"Hola mi nombre es { name }"
print('v3', template)


