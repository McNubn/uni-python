# Brian Doheny
# I initially attempted this myself by first understandind the algorithm and trying to work it out in Python.
# My own attempts at writing this function failed, and so I had to turn to a pre-written function, and studying that instead.
# I have been using the outline found at: https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo

# Define the fuction
def sqrt(x):
# Need to turn x into a new variable that we can run the algorithm on. i.e. a variable we can change now, so we can compare back to original later.
    r = x
# Precision allows us to decide what range of accuracy we want here.
# In this case it's to the power of minus 10, so accuracy down to 0.000000001
    precision = 10 ** (-10)

# Can use abs so that we're only dealing with the positive number here. 
# Makes the next step more simple, as we can ignore the negative square root.
# Here we're squaring our "r" figure and subtracting from x. If the result is greater than precision, than r cannot be the square root.
    while abs(x - r * r) > precision:
# This will run if the above is true, and so "r" is not the square root.
# We therefore change r to a new, smaller figure for the next attempt. In this case adding r to x, diving that by r, and then dividing that by 2.
# This gives us a new smaller r to try again with. This will keep going on until x-r*r is accurate to 0.000000001 
        r = (r + x / r) / 2
# When the program finds an r that is accurate to 0.000000001, the function will return it for use in remainder of the main program.
    return r