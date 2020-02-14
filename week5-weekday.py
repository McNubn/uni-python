# Brian Doheny
# Write a program that outputs whether or not today is a week day.

# Importing the datetime module. Guide on this module available at https://docs.python.org/2/library/datetime.html
import datetime

# Saving the current date to a variable called 'today'. 
today = datetime.datetime.now()

# Use the weekday function on the 'today' variable. This will return an integer between 0 (Monday) to 6 (Sunday). 
# The isoweekday() function could also be used, providing values between 1 (Monday) and 7 (Sunday). In this case the if condition would be ">= 6"
if today.weekday() >= 5:
    print ("It is the weekend, yay!")
else:
    print("Yes, unfortunately today is a weekday.")

    