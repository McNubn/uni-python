import math

def isprime(i):
   for j in range(2, math.floor(math.sqrt(i))):
        if i % j == 0:
            return False
        return True