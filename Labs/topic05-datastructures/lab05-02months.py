# Create a tuple that contains the months, then another with just the summer months.
# Print each of the summer months on a separate line.

# Tuple with all of the months included.
months = ('January','February','March','April','May','June','July','August','September','October','November','December')

# Splice months so that we get May, June and July saved to another tuple.
summer = months[4:7]

# For each item in summer, print it.
for i in summer:
    print(i)

# Confirmed that the new data type is a tuple.
# print(type(summer))