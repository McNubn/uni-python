# Write a function that prints out a menu of commands we can perform.
# i.e. add, vie wand quit. 
# The function should return what the user chose.

def menu():
    print("What would you like to do?") 
    print("\t (a) Add new student")
    print("\t (v) View students")
    print("\t (q) Quit")
    selection = input("Type one letter (a/v/q):").strip()

    return selection

selection = menu()
print("you chose {}".format(selection))
