spi = [0,3,4,5,6,7,9]

new_spi = []

for i in spi:
    new_spi.append(i**3)
print(new_spi)

def to_squre(x):
    return x**3
new_map = map(to_squre, spi)

print(list(new_map))