# Brian Doheny
# Turning that previous prime script into a function.

import myfunction
      
P = []

for i in range (2, 1000):
    if myfunction.isprime(i):
        P.append(i)

print(P)