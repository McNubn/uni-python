#This program will calculate the user's BMI score based of of their height and weight

height = float(input("Please enter your height (CMs): "))
weight = float(input("Please enter uour weight (KGs): "))

bmi = weight / ((height/100)**2)

print("Your BMI score is: ", bmi)
if bmi >= 30:
    print("This is classed as 'Obese' (BMI 30+)")
if 25 < bmi < 29.9:
    print ("This is classed as 'Overweight' (BMI 25-29.9)")
if 18.5 < bmi < 24.9:
    print("This is classed as 'Healthy' (BMI 18.5-24.9)")
if bmi <= 18.4:
    print ("This is classed as 'Underweight' (BMI less than 18.5)")