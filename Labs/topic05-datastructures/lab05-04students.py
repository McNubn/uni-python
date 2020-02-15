# Write a program that stores a student's name and a list of her courses, and grades in a dictionary.
# The program should then print out her data.

# Student info. Since the courses can change, we want to include them as a list.
# As each course has its own values - name & score for now, they'll need to be dictionaries
student = {
    'name': 'Mary',
    'courses': [
        {'courseName': 'Programming', 
        'score': 45},
        {'courseName': 'History', 
        'score': 99}
    ]
}


print('name: ', student['name'])

#  Wasn't getting the format quite right on my attempts to iterate in a for loop.

# for key in student['courses']:
   # print(key, ":", student[key])

for module in student["courses"]:
    print("\t {} \t: {}".format(module["courseName"], module["score"]))