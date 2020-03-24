# uni-python

Repository Layout

Weekly Assignments

The assignments for each week can be found in the root folder, alongside any other programs that may need to reside with them (i.e. the sqrt.py function for week 6). Each of the assignments includes the week it was set in the title, followed by the name of the program as requested by the assignment.

Lecture Content

Any additional programs set up while watching the lectures can be found in this folder. 

Labs

Attempts and final answers for the optional lab sheets can be found in this folder.

Assignments

Week 2 - BMI (week2-bmi.py)

This program asks the user to input their height in CM and their weight in KG, from this it will calculate their BMI. This is done by first converting the height in a measurement in metres (i.e. 192 cm = 1.92m), and then squaring this value. The weight is then divided by the squared height value to create the BMI. In my case I have rounded the final BMI figure to 2 decimal places, as additional decimal places seem unneccessary.

Week 3 - Second String (week3-secondstring.py)

This program initially asks the user to input a sentence as a string. It then outputs every second character in reverse. For this I've managed to condense the program down to one line of code that it it will immediately run the print on the user's input.

Week 4 - Collatz (week4-collatz.py)

This program asks the user to input any positive integer, and it will then perform some calculations on that integer and output the new valus until it eaches 1. If the value is even, it'll be divided by 2. If it is odd, it will be multiplied by 3 and then have 1 added to it. 

This is done via a while loop, so that it will keep iterating through the calculations until the value is 1. In the meantime each new value it creates on its way to 1 will be stored in a list, which is then printed to the terminal.

Week 5 - Weekday (week5-weekday.py)

This program makes use of the datetime module to check the current day of the week. If the day is Saturday or Sunday, it will say "It is the weekend, yay!" whereas if it is a weekday it will say "Yes, unfortunately today is a weekday." 

This is done by first assigning todays date (datetime.datetime.now()) to a variable, and checking if the weekday in that variable is greater than or equal to 5. As zero indexing is at play here, Saturday would be day 5, and Sunday would be day 6, therefore anything greater than or equal to 5 would be the weekend. If the value is not greater than or equal to 5, then it must be less than 5, and thus is a weekday, and so the else statement will run.

Week 6 - Squareroot (sqrt.py and week6-squareroot.py)

Description for this is split into two parts to describe what the function and program are doing.

a) sqrt.py

This function is based off an example found on https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo.

It takes the value x, and first creates a new variable from it called r. This allows us to perform calculations on r, while still keeping track of what x was initially. 

Alongside we also set a level of precision that we're comfortable with, and so in my case we went with a precision of 0.000000001. This means that once the program is within that range of the final answer, it won't go any further.

It then goes until a while loop, whereby as long as x minus r squared is larger than the precision variable it will perform the next step. That next step is to add r and x together, divide it by r, and then divde that by 2. This gives us a new next guess to run with, as the while loop is then performed on this new r figure. In the event that x minus r squared is less than the precision, we'll know we're close enough to declare r as the square root.

b) week6-squareroot.py

This program imports the above mentioned sqrt function, and requests the user to input a float. This float is then put through the sqrt function to return the approximate square root if the initial input.

Week 7 - E's (week7-es.py and eTest.txt)

This program creates and calls a function called countE. When CountE is called, the user will be requested to input a file name. That filename is then stripped of any spaces, and then opened in read only via with. It will then read the entire file in lower case, and count the number of "e"s in the file, and print that count out. In order to allow for easy testing of this program, I have included a txt file simply names eTest.txt.

Week 8 - Plotting (week8-plot.py)

This program plots the values of f(x)=x, g(x)=x squared and h(x)=x cubed within the range of 0 to 4 on one set of axes. To this it imports Numpy and PyPlot (from matplotlib). 

Numpy allows the program to generate an array of values from 0 to 4.1 (as the upper value is not included, I have set it to 4.1 so that 4 will be include in this) in steps of 0.5. The steps of 0.5 will allow for more markers on the plot, and thus give a bit of a smoother line. We use numpy arrays for this, as we can then square and cube the values in that array for g(x) and h(x).

It then uses pyplot to plot each of these three functions onto the same set of axes. Each function has the original numpy array as their x axis, and their respective function results on the y axis. These plots have also been labeled (with some use of Python's encoding to add the appropriate squared and cubed symbols - https://www.fileformat.info/info/unicode/char/b2/index.htm), alongside labels on the x and y axis, a title and a legend.