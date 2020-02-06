# Brian Doheny
# Write	a program (lab04.01-grade.py) that reads in a students percentage mark and prints out 
# corresponding	the	grade (the program should check	that the percentage	is valid)

score = float(input("Please enter your percentage mark. I will use this to find your grade."))
trueScore = round(score)

if 100 >= trueScore >= 70:
    print("Disctintion!")
elif 69 >= trueScore >= 60:
    print("Merit 1!")
elif 59 >= trueScore >= 50:
    print("Merit 2.")
elif 49 >= trueScore >= 40:
    print("Pass.")
elif trueScore < 40:
    print("Fail.")
else:
    print("That doesn't appear to be a correct score. Please ensure the percentage mark is between 0 and 100%, and try again.")