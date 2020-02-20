# Brian Doheny
# Turning that previous prime script into a function.

import math

def isprime(i):
   for j in range(2, math.floor(math.sqrt(i))):
        if i % j == 0:
            return False
        return True
      
P = []

for i in range (2, 1000):
    if isprime(i):
        P.append(i)

print(P)