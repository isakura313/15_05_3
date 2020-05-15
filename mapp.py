import random

data = ['shop', 'cup', 'third']

def func_add(tovar):
    return tovar + ": "+ str(random.randint(1, len(tovar)))
data_tovars = map(func_add, data)
print(list(data_tovars))
print(data)