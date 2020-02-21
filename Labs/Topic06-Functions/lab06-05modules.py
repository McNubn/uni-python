# Now to take in the modules. Want to keep asking for modules until user enters a blank modulen name.

students = []

def readModules():
    modules = []
    moduleName = input("enter the first Module name (blank to quit: ").strip()
    
    while moduleName != "":
        module = {}
        module["name"] = moduleName
        module["grade"] = int(input("\t\tEnter grade: "))
        modules.append(module)

        moduleName = input("\t Enter the next module name (blank to quit): ").strip()
    
    return modules

    

def doAdd():
    currentStudent = {}
    currentStudent["name"]=input("enter name: ")
    currentStudent["modules"]= readModules()

    students.append(currentStudent)

doAdd()
doAdd()
print(students)