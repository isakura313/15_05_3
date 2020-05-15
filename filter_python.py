a = [1,-4, 6, 8, -10]
def plus_number(x):
    if x > 0:
        return 1
    else:
        return 0
b = filter(plus_number, a)
b = list(b)
print(b)