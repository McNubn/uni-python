import random

x = int(input("Please enter the lower range: "))
y = int(input("Please enter the higher range: "))
number = random.randint(x, y)
print("Here is a random number: {}".format(number))