# Putting it all together now.

# students needs to be a global variable.
students = []

# Menu is defined, asks for input.
def menu():
    print("What would you like to do?") 
    print("\t (a) Add new student")
    print("\t (v) View students")
    print("\t (q) Quit")
    selection = input("Type one letter (a/v/q):").strip()
    return selection

# Add function for menu function is defined.
def doAdd():
    currentStudent = {}
    currentStudent["name"]=input("enter name: ")
    currentStudent["modules"]= readModules()
    students.append(currentStudent)

# Modules function for Add function is defined.
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

# New function to make modules nicer to view.
def displayModules(modules):
    print("\t Name \t Grade")
    for module in modules:
        print("\t{}   \t{}".format(module["name"],module["grade"]))

# View functions for the menu that calls the displayModules function
def doView():
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"])

# While loop to ensure that the menu keeps appearing if someone doesn't pick one of the 3 eligible options.
selection = menu()
while selection != "q":
    if selection == "a":
         doAdd()
    elif selection == "v":
        doView()
    elif selection != "q":
        print("\n\nplease selection a, v or q")
        selection=menu()