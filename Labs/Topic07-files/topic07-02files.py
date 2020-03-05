# Brian Doheny
# Create a program that counts how many times it was run.

# First open the file as read, and assign the count to a variable.
with open("count.txt","r") as f:
    count = f.read()

# Since I can't write in read-only mode, I am re-opening the file was write.
with open("count.txt","w") as f:
# Turn the count into an integer, and add 1 to make the new count.
    count = int(count) + 1
# Turn the new count back into a string and write it the file.
    f.write(str(count))

# Print the new value of count for confirmation.
print(count)