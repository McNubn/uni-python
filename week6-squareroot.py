# Brian Doheny
# Write a program that takes a positive floating-point number as input and 
# outputs an approximation of its square root.

import math

x = float(input("Please enter a positive number: "))

result = math.sqrt(x)
result = round(result,2)

print("The square root of {} is approx. {}.".format(x,result))