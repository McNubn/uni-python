# Brian Doheny
# Check if one number divides another

p = 8
m = 3

if p % m == 0:
    print(p, " divided by ", m, " leaves a remainder of zero.")
    print("I'll be run too if the condition is True.")
else:
    print(p, "divided by ", m, " does not leave a remainder of zero.")
    print("I'll be run too if the condition is False.")

# if p % m != 0:
    # print(p, "divided by ", m, " does not leave a remainder of zero.")

print("I'll be run no matter what!")