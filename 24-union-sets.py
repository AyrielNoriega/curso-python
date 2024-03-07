#union de conjuntos

set_a = {'col', 'mex', 'bol'}
set_b = {'ve', 'col', 'pe'}

set_c = set_a.union(set_b)
print(set_c)
'''o asi'''
print(set_a | set_b)

# intercepcion de conjuntos
set_a = {'col', 'mex', 'bol'}
set_b = {'ve', 'col', 'pe'}

set_c = set_a.intersection(set_b)
print(set_c)
'''o asi'''
print(set_a & set_a)

# diferencia en conjuntos; es una resta
set_a = {'col', 'mex', 'bol'}
set_b = {'ve', 'col', 'pe'}

set_c = set_a.difference(set_b)
print(set_c)
'''o asi'''
print(set_a - set_b)

# diferencia simetrica: union sin los elementos comunes
set_a = {'col', 'mex', 'bol'}
set_b = {'ve', 'col', 'pe'}
set_c = set_a.symmetric_difference(set_b)
'''o asi'''
print(set_a ^ set_b)