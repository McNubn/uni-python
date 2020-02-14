# Brian Doheny
# Request the user to input a String, and return every 2nd character backwards!

# Capturing the sentence from the user. According to https://www.edureka.co/blog/input-in-python, input will save it as an integer if a number alone is entered.
# I'm therefore restricting it to a string here. According to that website I could also use raw_input to only capture a string.
sentence = str(input("Please enter a sentence: "))

# In a real world example I'd have included additional text on the input function to let the user know we were going to mess with their sentence.
# I'd likely follow that up with another statement in between their input and the change to the string. e.g.:
# print("Watch this.")

# Prints the sentence backwards, and only showing every other letter. We want to start on the very last character, and go through to the very first
# so the first two arguments in the square brackets [] are not required.
print(sentence[::-2])