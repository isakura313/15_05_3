from simple_benchmark import benchmark
from recursia import recursia
from fact_cikl import fact_cikl

import matplotlib.pyplot as plt

func = [recursia, fact_cikl]
arguments = {}
for i in range(50):
    arguments['i'+ str(i)] = i
print(arguments)
arguments_name = 'natural numbers'

aliases = {fact_cikl: "Циклическая функция", recursia: "Рекурсия"}
b = benchmark(func, arguments, arguments_name, function_aliases= aliases)
b.plot()
plt.show(b)