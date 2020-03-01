# Brian Doheny
# Attempting to create a function that utilizes Newton's method for calculating square roots
# My understanding here is based off a 2 hour chat with a Maths graduate. Fingers crossed!

difference = 0.001

def recursive(x):
    y = square_root(x)

    while (y * y > (x + difference)) and (y * y < (x - difference)):
        x = y
        recursive(x)
    else:
        print(y)

        
def square_root(x):
  x = x - (x * x)/(2 * x)