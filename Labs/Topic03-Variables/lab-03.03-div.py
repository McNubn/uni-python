x = int(input("Please enter the first number: "))
y = int(input("Please enter the second number: "))

answer = x // y
remainder = x % y

print("{} divided by {} is {} with remainder {}".format(x, y, answer, remainder))