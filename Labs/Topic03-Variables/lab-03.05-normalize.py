words = str(input("Please enter a string: "))
lower = words.strip().lower()
x = len(words)
strip = words.strip()
y = len(strip)
print("That string normalized is: {}".format(lower))
print("We reduced your input string from {} to {} characters.".format(x,y))