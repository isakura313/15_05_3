import data

x = 14

def print_x():
    # global x
    # x = 12
    print(x)

print_x()
print(data.x)

def get_stepen(x):
    return x**2

def krat_3(x):
    if x%3 == 0:
        return("кратное 3")
    else:
        return "no"


print(krat_3(get_stepen(15)))