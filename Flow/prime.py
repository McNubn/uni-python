# Brian Doheny
# Check if a number is prime.
# The primes are 2, 3, 5, 7, 11, 13, ....

p = 222
m = 2
isprime = True

while m < p:
    if p % m == 0:
       # print(m, "divides", p, "and therefore", p, "is not prime.")
        isprime = False
        break
    m = m + 1

if isprime:
    print(p,"is a prime number!")
else:
    print(p, "is not a prime number!")
