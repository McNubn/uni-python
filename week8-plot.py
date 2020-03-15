# Brian Doheny
# Write a program that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 
# in the range [0, 4] on the one set of axes.

from matplotlib import pyplot as plt
import numpy as np

numbers = np.arange(0, 4.1, 0.5)
g = numbers ** 2
h = numbers ** 3

plt.plot(numbers,numbers)
plt.plot(numbers, g)
plt.plot(numbers, h)
plt.show()