func = lambda x, y: x + y
func_multiply = lambda x, y: x * y
print(func(2, 2))
print(func_multiply(3, 2))


def krat_3(x):
    if x%3 == 0:
        return("кратное 3")
    else:
        return "no"
func = lambda x: x**2

print(krat_3(func(2)))
