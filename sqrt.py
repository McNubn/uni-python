# Brian Doheny
# I have been using the outline found at: https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo
# A full rundown of this function can be found in the README.

def sqrt(x):
# Creating a new variable based on x, so that we can perform calcutions on r without changing the original input.
    r = x
# Setting precision to 0.000000001, as this will give us a good level of accuracy.
    precision = 10 ** (-10)

# Since we're only calculating with the positive integer, we can use abs here.
# if (x - r * r) is greater than the precision, the while loop will run the next calculation to set a new value for r.
# if (x - r * r) is less than the precision, the while loop will just return r, as the accuracy is close enough.
    while abs(x - r * r) > precision:
        r = (r + x / r) / 2
    return r