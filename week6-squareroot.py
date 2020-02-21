# Brian Doheny
# Write a program that takes a positive floating-point number as input and 
# outputs an approximation of its square root.

# Will use the Math module for now until I clarify if I need to make my own function here.
import math

# Asking the user to input a floating point number.
x = float(input("Please enter a positive number: "))

# Take their result and run the math.sqrt function on it.
result = math.sqrt(x)
# Rounding the answer to 2 decimal places - makes it a bit tider.
result = round(result,2)
# And print the result, letting the user know their initial input and the square root of it.
print("The square root of {} is approx. {}.".format(x,result))