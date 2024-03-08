# Higher order function: una función dentro de otra función
def increment(x):
    return x + 1

def highOrdFunct(x, func):
    return x + func(x)

result = highOrdFunct(2, increment)
print(result)