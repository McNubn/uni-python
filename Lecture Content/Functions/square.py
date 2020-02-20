# Brian Doheny
# A function to square numbers

# here f is the function name. Can be anything, e.g. "square" since names should be descriptive
# Can have multiple inputs, just x in this case. These inputs are called "arguments".
def f(x):
    ans = x * x
    return ans

# ans is local to this function - the variable only exists inside this function. 
# This is shown by the indentation.

# print(f(5))
# print(f(4))

# Here's an example with two arguments, x and y.
# Functions can include loops - e.g. for and while loops.

def power(x,y):
    ans = x
    y = y - 1
    while y > 0:
        ans = ans * x
        y = y - 1
    return ans

print(power(5,7))