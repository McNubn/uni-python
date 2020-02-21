# If a is selected, have it start a function called doAdd.
# If v is selected, have it start a functioned called doView
# If q is selected, end.

def menu():
    print("What would you like to do?") 
    print("\t (a) Add new student")
    print("\t (v) View students")
    print("\t (q) Quit")
    selection = input("Type one letter (a/v/q):").strip()

    return selection

selection = menu()
print("you chose {}".format(selection))

def doAdd():
    print("Under construction...")

def doView():
    print("Also under construction...")

while selection != "q":
    if selection == "a":
         doAdd()
    elif selection == "v":
        doView()
    elif selection != "q":
        print("\n\nplease selection a, v or q")
    selection=menu()