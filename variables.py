#Brian Doheny
#Checking out variables

x = 911
y = 2

z = x + y

print(z)

fac = 7 * 6 * 5 * 4 * 3 * 2 * 1
print(fac)

s = "Brian's wonderful adventures!"

#Slicing the string - first value is the start point (0 is first character), 
#second value is the end point.
print(s[0:17])
#Just returnining every 3rd character in the splice.
print(s[0:17:3])

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(l)
#Similar to String slice - this will return the 4th item in the list (remember 1st place = 0)
print(l[3])
print(l[2:6:3])