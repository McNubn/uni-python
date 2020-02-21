# Create the doAdd() function.
# Read in the students name
# Read in the module names and grades
# test the function
# add the student dict to an array
# test

students = []

def readModules():
    return []

def doAdd():
    currentStudent = {}
    currentStudent["name"]=input("enter name: ")
    currentStudent["modules"]= readModules()

    students.append(currentStudent)

doAdd()
doAdd()
print(students)