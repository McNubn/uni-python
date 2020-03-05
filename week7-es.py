# Brian Doheny
# Write a program that reads a text file and outputs the number of e's it contains.
# The program should take the filename from an argument on the command line.

# Since we're asked to load the filename as an argument, I created this as a function.

def countE(filename):
    # Want to ensure there's no trailing spaces that might mess up the filepath, so I'm using strip.
    filename = str(filename.strip())
    # Using "with" to ensure that the file is closed afterwards. Opening in read-only mode as I am not looking to write.
    with open((filename), 'r') as theFile:
        # Need to actually read the file, and as we're counting a particular character, I want everything to be uniform.
        # In this case I'm making the whole file lower case, so that normally capitalized e's will also be counted.
        theFile = theFile.read().lower()
        # Here we're just counting the number of e's and printing it. Copying the format of the problem's example answer. 
        print(theFile.count("e"))
# Not quite sure how to add the argument into the function without separately requesting user input. Might come back to this.
countE(input())