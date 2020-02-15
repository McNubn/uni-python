# Create a program that puts 10 random numbers into a queue (list)
# The program will then output all of the values in the queue
# Then take the next number out of the queue, print it and the remaining numbers in the queue
# pop(0) will help here

# Importing randint so I can make random integers
from random import randint

# Create the list that will hold those integers
queue = []

# Create 10 random integers between 0 and 100.
for x in range(10):
    queue.append(randint(0,100))

# Print the current state of the queue.
print("queue is ", queue)

# For each item in the queue, pop the first item, and print it with the current queue.
for number in queue:
    picked = queue.pop(0)
    print('current queue Number is ', picked, ' and the queue is ', queue)
    if len(queue) == 0:
        break



print('the queue is now empty')