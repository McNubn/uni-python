# Brian Doheny
# Write a program that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 
# in the range [0, 4] on the one set of axes.

# Improting pyplot for the plots themselves. Numpy to create an array to square and cube.
from matplotlib import pyplot as plt
import numpy as np

# Letting numpy create the array. Set the higher limit at 4.1 so that 4.0 will be included.
# Got this tip from https://realpython.com/how-to-use-numpy-arange/#providing-all-range-arguments
numbers = np.arange(0, 4.1, 0.5)
# Squaring and cubing the array, and saving them to variables for plotting.
g = numbers ** 2
h = numbers ** 3

plt.plot(numbers,numbers, label = "f(x)=x")
# Found out how to format the squared and cubed characters via https://www.fileformat.info/info/unicode/char/b2/index.htm
plt.plot(numbers, g, label = "g(x)=x" +  u"\u00B2")
plt.plot(numbers, h, label = "h(x)=x" + u"\u00B3")
# Now to add labels and titles to make it as clear as possible.
plt.xlabel("Value of x")
plt.ylabel("Result of function")
plt.title("Results of f(x)=x, g(x)=x" + u"\u00B2" + " and h(x)=x" + u"\u00B3")
# Adding a legend that'll utilise the labels for each plot that I set above.
plt.legend()
plt.show()