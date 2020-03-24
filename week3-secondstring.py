# Brian Doheny
# Request the user to input a String, and return every 2nd character backwards!

# Capturing the sentence from the user. According to https://www.edureka.co/blog/input-in-python, input will save it as an integer if a number alone is entered.
# I'm therefore restricting it to a string here. According to that website I could also use raw_input to only capture a string.
# I've since condensed this down to on line by including the initial input into a print function, along with the slicing of the input string..
print(str(input("Please enter a sentence: "))[::-2])
