# Brian Doheny
# Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. 
# At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, 
# multiply it by three and add one. Have the program end if the current value is one.


x = int(input("Please enter a positive number, and I'll do some magic here for you."))

while x > 1:
    if x % 2 == 0:
        x = x / 2
        print("The number is even, so now I'm going to half it to make", x)
    else:
        x = (x * 3) + 1
        print("The number is odd, so now I'm going to triple it and add 1 to make", x)
else:
    print("And that brings us to 1. Job done. Goodnight!")