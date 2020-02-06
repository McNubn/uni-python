# Brian Doheny
# Write a program that reads in students until the user enters blank in as the student's first name.
# The program should then print out all the students entered in a neat way.

students = []

firstname = input("Please enter the student's first name (or leave blank to exit this program):").strip().capitalize()

while firstname != "":
    student = {}
    student["firstname"] = firstname
    lastname = input("Please enter the student's surname:").strip().capitalize()
    student["lastname"] = lastname
    students.append(student)

    firstname = input("Please enter the student's first name (or leave blank to exit this program):").strip().capitalize()

print("The students you have entered are:")
for currentStudent in students:
    print("{} {}".format(currentStudent["firstname"],currentStudent["lastname"]))