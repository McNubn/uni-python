# Brian Doheny
# Write a program that takes a positive floating-point number as input and 
# outputs an approximation of its square root.

# Importing the sqrt function from the sqrt file.
from sqrt import sqrt

# Ask user to input a float, save it to x for use in the sqrt function.
x = float(input("Please enter a positive number: "))
result = sqrt(x)
# Rounding the answer to 1 decimal places - makes it a bit tidier, and brings it inline with sample answer.
result = round(result,1)
# And print the result, letting the user know their initial input and the square root of it.
print("The square root of {} is approx. {}.".format(x,result))