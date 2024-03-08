# funciones anónimas
'''funcion normal'''
def increment(x):
    return x + 1

result = increment(10)
print(11)

'''funcion lambda'''
x = lambda x : x + 1
print(x(5))

'''funcion lambda'''
fullName = lambda name,  lastName : f'Your full name is { name } { lastName }'
print(fullName('Ayriel', 'Noriega'))