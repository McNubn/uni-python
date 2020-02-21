# Brian Doheny
# Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. 
# At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, 
# multiply it by three and add one. Have the program end if the current value is one.

# Request the user to enter a positive integer. Capturing it as an integer, to ensure that they do not enter a string.
number = int(input("Please enter a positive integer: "))
# In order to print the results in 1 line, like the example, I will add them to a list. I may revise this later (note - Whirldwind tour of python page 38 "for loops" section had a better solution)
calculations = []

while number > 1:
    if number % 2 == 0:
        number = number / 2
        # With the division involved, the integers are changing to floats. As only even numbers are being divided, I can keep everything as an integer
        # without losing anything.
        calculations.append(int(number))
        # In a real scenario I'd consider adding some element to provide the user context on what is happening in the calculations, such as: 
        # print("The number is even, so now I'm going to half it to make", number)
    else:
        number = (number * 3) + 1
        calculations.append(int(number))
        # print("The number is odd, so now I'm going to triple it and add 1 to make", number)
else:
    # Got the idea to iterate through the list like this from page 38 in Whirldwind Tour of Python.
   for x in calculations:
        print(x, end =' ')