# This program calculates how many tiles you will need 
# when tiling a wall or floor in metres squad

length = float(input("Please enter room length in metres: "))
width = float(input("Please enter room width in metres: "))

area = length * width

needed = area * 1.05

print("You need ", needed, " tiles in metres squared.")