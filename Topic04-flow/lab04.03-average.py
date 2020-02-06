# Brian Doheny
# Write a program that keeps reading numbers until the user enters a 0.
#The program should then print out each of the numbers entered, and the average of them.

x = int(input("Enter a number! I'll stop if you enter 0: "))
xlist =[]

while x != 0:
    xlist.append(x)

    x = int(input("Enter a number! I'll stop if you enter 0: "))

for value in xlist:
    print(value)

average = float(sum(xlist)) / len(xlist)
print("The average is {}".format(average))